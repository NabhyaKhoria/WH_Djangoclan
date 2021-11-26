#Django imports
from django import urls
from django.urls import path, include

# Standard Package Imports

# Project Imports
from . import views


# Third Party Imports


app_name = 'event'

urlpatterns = [
    path('event', views.eventhome, name='eventhome'),
    
    # path('viewMembers', views.viewmembers, name='viewMembers'),
    # path('members/<name>', views.members, name='members'),
    # path('publications', views.publications, name='publications'),
    # path('form', views.form, name='form'),
    # path('viewmembers', views.viewmembers, name='viewmembers'),
    # path('subjects/<name>', views.subjects, name='subjects'),
    # path('aiml/<name>', views.aiml, name='aiml'),
    #path('get_quote/', views.get_quote, name='get_quote'),
    # path('<int:year>/', views.diary),
    # path('<int:year>/<str:name>/', views.diary),
]