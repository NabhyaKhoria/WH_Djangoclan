from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
import csv
from django.http import HttpResponse
from .models import *

admin.site.register(Profile)
admin.site.register(Society)
admin.site.register(Achivement)