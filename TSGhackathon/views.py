from django.shortcuts import render,redirect
import math, random
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from event.models import *
import openpyxl


def home(request):
    return render(request, 'nav.html')


def base(request):
    studentWelfare = StudentWelfare.objects.all()
    technologys = Technology.objects.all()
    socials = Social.objects.all()
    sports = Sports.objects.all()

    context = {
        'studentWelfare': studentWelfare,
        'technologys':technologys,
        'socials':socials,
        'sports':sports,
    }
    return render(request, 'base.html', context)

def login(request):
    if(request.method == 'POST'):
        OTP = ""
        email = request.POST['signin-email']
        wb_obj = openpyxl.load_workbook("media\student\Student Data.xlsx")
        sheet_obj = wb_obj.active
        semail=[]
        for j in range(3,sheet_obj.max_row+1):
            cell_obj = sheet_obj.cell(row = j, column = 1)
            semail.append(cell_obj.value)
        val=0
        print(semail)
        if semail.count(email):
            val=1
            string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            length = len(string)
            for i in range(6) :
                OTP += string[math.floor(random.random() * length)]
            subject = 'One Time Password (OTP) to login at TSG'
            email2 = EmailMessage(
                            subject, OTP, settings.EMAIL_HOST_USER, to=[email]
                        )
            email2.send(fail_silently=True)
        return render(request,'baselogin.html', {'email':email,'OTP':OTP,'val':val})
    else:
        return render(request,'base.html')

def loginuser(request):
    if(request.method == 'POST'):
        email = request.POST['signin-email']
        OTP=""
        return render(request,'baselogin.html', {'email':email,'OTP':OTP})
    else:
        return render(request,'base.html')