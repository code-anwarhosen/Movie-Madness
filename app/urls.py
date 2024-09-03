from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('series/<str:pk>/', views.series, name='series'),
    path('search/', views.search, name='search'),
    path('player/<str:pk>/', views.player, name='player'),
]
