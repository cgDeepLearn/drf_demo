#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 10:50
# @Author  : cgDeepLearn
# @Email   : cglearningnow@163.com
# @File    : urls.py


from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),
         name="snippet-highlight"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
