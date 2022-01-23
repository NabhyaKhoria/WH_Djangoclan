#Django imports
from django import urls
from django.urls import path, include



# Standard Package Imports

# Project Imports
from . import views


# Third Party Imports


app_name = 'event'

urlpatterns = [
    path('official_dashboard', views.dashboard, name='dashboard'),
    path('official_dashboard/add_social', views.dashboard_add_social, name='dashboard_add_social'),
    path('official_dashboard/view_social/(?P<pk>[0-9a-f-]+)', views.dashboard_view_social, name='dashboard_view_social'),
    path('official_dashboard/del_social/(?P<pk>[0-9a-f-]+)', views.dashboard_del_social, name='dashboard_del_social'),
    path('official_dashboard/add_sports', views.dashboard_add_sports, name='dashboard_add_sports'),
    path('official_dashboard/view_sports/(?P<pk>[0-9a-f-]+)', views.dashboard_view_sports, name='dashboard_view_sports'),
    path('official_dashboard/del_sports/(?P<pk>[0-9a-f-]+)', views.dashboard_del_sports, name='dashboard_del_sports'),  
    path('official_dashboard/add_studentwelfare', views.dashboard_add_studentwelfare, name='dashboard_add_studentwelfare'),
    path('official_dashboard/view_studentwelfare/(?P<pk>[0-9a-f-]+)', views.dashboard_view_studentwelfare, name='dashboard_view_studentwelfare'),
    path('official_dashboard/del_studentwelfare/(?P<pk>[0-9a-f-]+)', views.dashboard_del_studentwelfare, name='dashboard_del_studentwelfare'),
    path('official_dashboard/add_technology', views.dashboard_add_technology, name='dashboard_add_technology'),
    path('official_dashboard/view_technology/(?P<pk>[0-9a-f-]+)', views.dashboard_view_technology, name='dashboard_view_technology'),
    path('official_dashboard/del_technology/(?P<pk>[0-9a-f-]+)', views.dashboard_del_technology, name='dashboard_del_technology'),
    path('technology', views.technology, name='technology'),
    path('SocialandCulture', views.social, name='social'),
    path('SportsandGames', views.sports, name='SportsAndGames'),
    path('Studentswelfare', views.studentWelfare, name='studentWelfare'),
    path('technology/<name>', views.technology_details, name='technology'),
    path('studentWelfare/<name>', views.studentWelfare_details, name='studentWelfare'),
    path('SocialandCulture/<name>', views.social_details, name='social'),
    path('SportsandGames/<name>', views.sports_details, name='sports'),
    path('Results', views.result, name='result'),
    path('interIIT', views.interIIT, name='interIIT'),
    path('interIIT-Technology', views.interIITtechnology,name='interIIT-Technology'),
    path('interIITSocult', views.interIITsocult, name='interIIT-socult'),
    path('GCTechnology', views.GCTechnology, name='GCTechnology'),
    path('GCSocult', views.GCSocult, name='GCSocult'),
]
