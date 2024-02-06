from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('producer',views.producer),
    path('getAllItems',views.getAllItems),
]