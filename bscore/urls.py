from django.urls import path

from . import views

urlpatterns = [
    path('difference', views.difference, name='difference'),
]