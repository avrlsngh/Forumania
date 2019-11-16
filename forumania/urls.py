from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^connect/', include('connect.urls')),
    url(r'about/$', views.about),
    url(r'^$', views.homepage, name="homepage")
]

urlpatterns += staticfiles_urlpatterns()
