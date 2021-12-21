from django.shortcuts import render
from django.http import HttpResponse
from event.models import *

from django.core.paginator import PageNotAnInteger, Paginator
# Create your views here.


def eventhome(request):
    context = {
    }
    return render(request, 'events/base.html', context)

def technology(request):
    technology = Technology.objects.all()
    # context = {
    #     'technology': technology, 
    # }
    p=Paginator(technology, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context={
        'technology': technology,
        'page_obj': page_obj,
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
    # context = {
    #     'social': social,
    # }
    p=Paginator(social, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context={
    'social': social,
    'page_obj': page_obj,
    }
    return render(request, 'events/SocialCulture.html', context)



def studentWelfare(request):
    studentWelfare = StudentWelfare.objects.all()
    # context = {
    #     'studentWelfare': studentWelfare,
    # }
    p=Paginator(studentWelfare, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context={
    'studentWelfare': studentWelfare,
    'page_obj': page_obj,
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
    # context = {
    #     'sports': sports,
    # }
    p=Paginator(sports, 6) # creating paginator objects
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) # returns desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj=p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context={
    'sports': sports,
    'page_obj': page_obj,
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
    return render(request, 'results/index.html', context)



# def listing(request):
#     studentWelfare = StudentWelfare.objects.all()
#     technologys = Technology.objects.all()
#     socials = Social.objects.all()
#     sports = Sports.objects.all()

#     context = {
#         'studentWelfare': studentWelfare,
#         'technologys':technologys,
#         'socials':socials,
#         'sports':sports,
#     }
#     paginator = Paginator(context, 6) # Show 6 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'technology.html', {'page_obj': page_obj})

