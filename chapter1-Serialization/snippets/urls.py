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
    path('', views.snippet_list, name='snippet_list'),
    path(r'<int:pk>/', views.snippet_detail, name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)