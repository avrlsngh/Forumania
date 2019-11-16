from django.shortcuts import render, redirect
from connect.models import Post, Comment
from django.db.models import Q
from . import forms
from django.http import HttpResponse
from .filters import PostFilter 
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def connect(request):
    if request.method == 'POST':
        form = forms.UploadContent(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('connect:home')
    else:
        form = forms.UploadContent()
        posts = Post.objects.all().order_by('created_at')
        posts_filter = PostFilter(request.GET, queryset=posts)
    return render(request, 'connect/connect.html',{'form':form, 'posts': posts, 'filter': posts_filter})

@login_required(login_url="/accounts/login")
def post_detail(request, id):
    post = Post.objects.get(id=id)
    post.views = post.views + 1
    post.save()
    comments = []
    comment_count = 0
    if len(Comment.objects.all()) != 0 :
        comments = Comment.objects.filter(post=post)
        comment_count = comments.count()
    comment_form = forms.CommentForm()
    return render(request, 'connect/post_detail.html', {'post': post, 'comment_form':comment_form, 'comments': comments, 'comment_count': comment_count})

@login_required(login_url="/accounts/login")
def add_comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            post.comment_count = post.comment_count + 1
            post.save()
            return redirect('connect:detail', id=id)
