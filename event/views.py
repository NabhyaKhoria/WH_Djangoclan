from django.shortcuts import render
from django.http import HttpResponse

from event.models import *

# Create your views here.


def eventhome(request):
    context = {
    }
    return render(request, 'events/base.html', context)

def technology(request):
    technology = Technology.objects.all()
    context = {
        'technology': technology,
    }
    return render(request, 'events/technology.html', context)

def technology_details(request, name):
    technology = Technology.objects.get(name=name)
    context = {
        'technology': technology,
    }
    return render(request, 'events/technology_details.html', context)

def sac(request):
    context = {}
    return render(request, 'events/SocialCulture.html', context)

def sports(request):
    context = {}
    return render(request, 'events/SportsAndGames.html', context)

def welfare(request):
    context = {}
    return render(request, 'events/studentWelfare.html', context)

