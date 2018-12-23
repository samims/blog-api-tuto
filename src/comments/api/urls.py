from django.conf.urls import url

from django.contrib import admin

from .views import (CommentListAPIView, CommentDetailAPIView)

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/delete/$', CommentDetailAPIView.as_view(), name='detail')
]
