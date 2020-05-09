__author__ = "CunjunWang <cw3199@columbia.edu>"
__date__ = "2020/5/9"

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.realtor_list, name='list'),
    path('<int:realtor_id>', views.detail, name='detail')
]
