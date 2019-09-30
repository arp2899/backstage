from django.urls import path

from . import views

urlpatterns = [
    path('difference', views.difference, name='difference'),
    path('pythagorean-triplets', views.pythagorean_triplets, name='pythagorean_triplets'),
]