from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # В случае кэшировании класса -> path('', cache_page(60)(UnitsView.as_view()), name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.UnitDetailView.as_view(), name='detail_view'),
    path('<int:pk>/update', views.UnitUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', views.UnitDelete.as_view(), name='delete_view'),
    path('register', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    #path('admin/', views.dom, name='home'),
]

