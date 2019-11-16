from django.conf.urls import url
from . import views

app_name = "connect"
   
urlpatterns = [
    url(r'^$', views.connect, name="home"),
    url(r'^(?P<id>[\w-]+)/$', views.post_detail, name="detail"),
    url(r'^add_comment/(?P<id>[\w-]+)/$', views.add_comment, name="add_comment"),
]
