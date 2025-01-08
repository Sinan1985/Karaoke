from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.test, name='test'),
    path('', views.enter_song, name='enter_song'),
    path('songs_list/', views.songs_list, name='songs_list'),
    path('enter_song/', views.enter_song, name='enter_song'),

]