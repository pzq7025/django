"""
    this py file is copy from the file of name is myblog
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]