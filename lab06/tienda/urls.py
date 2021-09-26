from django.contrib import admin
from django.urls import path
from . import views

APP_NAME='tienda'

urlpatterns = [
    path('', views.index,name='index'),
    path('producto/<int:producto_id>/', views.producto,name='producto'),
    path('categoria/<str:categoria_nombre>/', views.categoria,name='categoria')
]
