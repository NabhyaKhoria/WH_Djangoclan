#Django imports
from django import urls
from django.urls import path, include



# Standard Package Imports

# Project Imports
from . import views


# Third Party Imports


app_name = 'event'

urlpatterns = [
    
    path('technology', views.technology, name='technology'),
    path('Social and Culture', views.sac, name='SocialCulture'),
    path('Sports and Games', views.sports, name='SportsAndGames'),
    path('Students welfare', views.welfare, name='welfare'),
    path('eventdetail', views.eventdetail, name='eventdetail'),
    
    
]