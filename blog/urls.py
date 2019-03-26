'''
Created on Oct 21, 2018

@author: leonardo
'''

from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_text/<int:pk>/<int:pkk>/<str:pkkk>/', views.post_text, name='post_text'),
    path('test/<int:pk>/', views.test, name='test'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
