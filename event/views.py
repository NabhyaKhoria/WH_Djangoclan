from django.shortcuts import render

# Create your views here.


def eventhome(request):
    context = {
    }
    return render(request, 'events/base.html', context)

def technology(request):
    context = {}
    return render(request, 'events/technology.html', context)

def sac(request):
    context = {}
    return render(request, 'events/SocialCulture.html', context)

def sports(request):
    context = {}
    return render(request, 'events/SportsAndGames.html', context)

def welfare(request):
    context = {}
    return render(request, 'events/studentWelfare.html', context)

def eventdetail(request):
    context = {}
    return render(request, 'events/event-details.html', context)