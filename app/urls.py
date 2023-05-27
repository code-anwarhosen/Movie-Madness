from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('player/<str:pk>/', views.player, name='player'),
]
