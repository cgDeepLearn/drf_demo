#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 10:50
# @Author  : cgDeepLearn
# @Email   : cglearningnow@163.com
# @File    : urls.py


from django.urls import path
# from snippets import views  # 使用api_view装饰器
# from snippets import views_usingmixins as views  # 使用mixins
from snippets import views_class_based as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippet_list'),
    path(r'<int:pk>/', views.SnippetDetail.as_view(), name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)