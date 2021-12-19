import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import *

Role = (
    ('Admin','ADMIN'),
    ('Tsg Official', 'TSG OFFICIAL'),
    ('Governer','GOVERNER'),
    ('Student','STUDENT'),
    )
    
class Society(models.Model):
    fullname = models.CharField(max_length=250, null=True)


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=250, null=True)
    rollno = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=30, choices=Role, default='Student')
    societies=models.ManyToManyField(Society, blank=True)
    
    def __str__(self):
        return str(self.fullname) + str(' | ') + self.role

