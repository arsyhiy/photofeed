from django.urls import path, include
from . import views

urlpatterns = [
  path('index', views.index, name='index'),
  path('feed/', views.imagelistView.as_view(), name='images'),
]

