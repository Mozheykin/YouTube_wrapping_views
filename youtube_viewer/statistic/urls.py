from django.urls import path
from .views import statistic, not_found, delete, add_video, change, Play

urlpatterns = [
    path('', statistic, name='main'),
    path('404/', not_found, name='not_found'),
    path('add/', add_video, name='add'),
    path('delete/<str:pk>/', delete, name='delete'),
    path('change/<str:pk>/', change, name='change'),
    path('play/', Play, name='play'),
]
