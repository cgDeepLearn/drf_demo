#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 10:50
# @Author  : cgDeepLearn
# @Email   : cglearningnow@163.com
# @File    : urls.py


# using routers
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]


'''
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', api_root),
    path('snippets/', snippet_list, name="snippet-list"),
    path('snippets/<int:pk>/', snippet_detail, name="snippet-detail"),
    path('snippets/<int:pk>/highlight/',snippet_highlight,
         name="snippet-highlight"),
    path('users/', user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
