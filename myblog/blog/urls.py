"""
    this py file is copy from the file of name is myblog
"""
from django.urls import path, re_path
from django.conf.urls import url
from . import views

# 2.0版本以后用re_path来创建
"""
response the name is views of function
the app_name is required parameter
"""
app_name = 'blog'
urlpatterns = [
    re_path(r'^index/$', views.index),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    re_path(r'^edit/action$', views.edit_action, name='edit_action'),
]