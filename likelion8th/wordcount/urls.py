from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.wordcount, name = "wordcount"),
    path('about',views.about, name = "about"),
    path('result/',views.result, name="result"),
    path('apples', views.apple, name="apples"),
]