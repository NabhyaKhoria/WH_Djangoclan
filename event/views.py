from django.shortcuts import render

# Create your views here.


def eventhome(request):
    context = {
    }
    return render(request, 'events/base.html', context)