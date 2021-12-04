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

def social(request):
    social = Social.objects.all()
    context = {
        'social': social,
    }
    return render(request, 'events/SocialCulture.html', context)



def studentWelfare(request):
    studentWelfare = StudentWelfare.objects.all()
    context = {
        'studentWelfare': studentWelfare,
    }
    return render(request, 'events/studentWelfare.html', context)


def social_details(request, name):
    social = Social.objects.get(name=name)
    context = {
        'social': social,
    }
    return render(request, 'events/social_details.html', context)

def studentWelfare_details(request, name):
    studentWelfare = StudentWelfare.objects.get(name=name)
    context = {
        'studentWelfare': studentWelfare,
    }
    return render(request, 'events/studentWelfare_details.html', context)

def sports(request):
    sports = Sports.objects.all()
    context = {
        'sports': sports,
    }
    return render(request, 'events/SportsAndGames.html', context)

def sports_details(request, name):
    sports = Sports.objects.get(name=name)
    context = {
        'sports': sports,
    }
    return render(request, 'events/sports_details.html', context)

def result(request):
    context={

    }
    return render(request, 'events/results.html', context)
