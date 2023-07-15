
from django.urls import path
from . import views 
urlpatterns = [

    path('', views.home, name='homepage'),
    path('video',views.youtube_videos, name='video'),
    path('shorts',views.shorts,name='shorts'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    
    ]