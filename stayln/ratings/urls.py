#! /usr/bin/python3

__author__ = "CunjunWang <cw3199@columbia.edu>"
__date__ = "2020/5/10"

from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_rating, name='add'),
]
