from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    views = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=250, default=None, null=False, blank=False)
    content = models.TextField()
    comment_count = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)

    def snippet(self):
        return self.content[:50] + '...'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey('connect.Post', on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.user)