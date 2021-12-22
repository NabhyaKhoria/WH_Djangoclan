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
    path('SocialandCulture', views.social, name='social'),
    path('SportsandGames', views.sports, name='SportsAndGames'),
    path('Studentswelfare', views.studentWelfare, name='studentWelfare'),
    path('technology/<name>', views.technology_details, name='technology'),
    path('studentWelfare/<name>', views.studentWelfare_details, name='studentWelfare'),
    path('SocialandCulture/<name>', views.social_details, name='social'),
    path('SportsandGames/<name>', views.sports_details, name='sports'),
    path('Results', views.result, name='result'),
]
