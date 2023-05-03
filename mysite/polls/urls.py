from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getform/', views.StudentsFormUpdate, name='getform'),
    path('home/', views.home,name='home'),
    path('dom/', views.dom,name='dom'),
    #path('admin/', views.dom, name='home'),
]