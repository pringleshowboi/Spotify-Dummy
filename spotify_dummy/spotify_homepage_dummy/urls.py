from django.urls import path, include
from . import views

app_name = 'spotify_homepage_dummy'
urlpatterns = [
    path('', views.home, name='home'),
    path('songs/<int:playlist_id>/', views.songs, name='songs'),
]
