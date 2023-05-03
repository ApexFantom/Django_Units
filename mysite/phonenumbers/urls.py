from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.pn, name='pn'),
    #path('admin/', views.dom, name='home'),
]