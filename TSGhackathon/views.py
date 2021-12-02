from django.shortcuts import render,redirect
import math, random
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def home(request):
    return render(request, 'nav.html')


def base(request):
    return render(request,'base.html')

def login(request):
    if(request.method == 'POST'):
        email = request.POST['signin-email']
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        OTP = ""
        length = len(string)
        for i in range(6) :
            OTP += string[math.floor(random.random() * length)]
        subject = 'One Time Password (OTP) to login at TSG'
        email2 = EmailMessage(
						subject, OTP, settings.EMAIL_HOST_USER, to=[email]
					)
        email2.send(fail_silently=True)
        return render(request,'baselogin.html', {'email':email,'OTP':OTP})
    else:
        return render(request,'base.html')

def loginuser(request):
    if(request.method == 'POST'):
        email = request.POST['signin-email']
        OTP = ""
        return render(request,'baselogin.html', {'email':email,'OTP':OTP})
    else:
        return render(request,'base.html')
