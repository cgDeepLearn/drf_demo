#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 13:24
# @Author  : cgDeepLearn
# @Email   : cglearningnow@163.com
# @File    : views_class_based.py


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer