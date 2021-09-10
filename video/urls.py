from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from video.views import get_url
urlpatterns = [
    path('getUrl',get_url),
]