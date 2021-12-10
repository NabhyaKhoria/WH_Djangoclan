from django.shortcuts import render,redirect
import math, random
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from event.models import *
import openpyxl
from datetime import date

def home(request):
    return render(request, 'nav.html')


def base(request):
    if request.user.is_authenticated:
        print(request.user)
        print("USer Successfullyy logged in ")
    else:
        print("User Login Failed")
    studentWelfare = StudentWelfare.objects.all().order_by('date')
    technologys = Technology.objects.all().order_by('date')
    socials = Social.objects.all().order_by('date')
    sports = Sports.objects.all()

    events = []
    for stud in studentWelfare:
        events.append(stud)

    for stud in technologys:
        events.append(stud)

    for stud in socials:
        events.append(stud)

    for stud in sports:
        events.append(stud)
        
    now = date.today()
    date_new = []
    event2 = []
    for event in events:
        date_new.append(event.date)

    date_new.sort()

    for i in range(len(events)):
        for stu in events:
            if date_new[i] == stu.date:
                event2.append(stu)
                break
            else:
                pass

    student = []
    var_new = 0
    for event in event2:
        if event.date >= now:
            student.append(event)
            var_new += 1
        if var_new == 3:
            break

    context = {
        'student': student,
        'events': events,
        'studentWelfare': studentWelfare,
        'technologys':technologys,
        'socials':socials,
        'sports':sports,
    }
    return render(request, 'base.html', context)


def login1(request):
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
        OTP=request.POST['rotp']
        gotp=request.POST['otp']
        if OTP==gotp:
            print("success")
            # print(User.objects.get(email=request.POST.get("signin-email")))
            # print(User.objects.get(email=email))
            try :
                a=User.objects.get(email=email)
                print(a)
                print("success101")
                b=authenticate(username=email,password="1234")
                print(b)
                print('success103')
                if b is not None:
                    login(request, b)
                    print('success104')
                else:
                    login(request, a)
                    print('success105')
            except:
                print("success102")
                user=User.objects.create(email=email)
                user.save()

                login(request, user)

            if request.user.is_authenticated:
                print('SUCCESS AGAIN')
                return redirect('base')  
                
            
            
        else:
            print("fail")
    else:
        return render(request,'base.html')  