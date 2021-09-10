from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('stream',views.stream_download),
]