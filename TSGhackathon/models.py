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

Category = (
    ('Technology','Technology'),
    ('Social_Culture','Social_Culture'),
    ('Sports_Games','Sports_Games'),
    ('Student_Welfare','Student_Welfare'),
    ('Others','Others'),
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


class Achivement(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=30, choices=Category, default='Technology')
    image = models.ImageField(upload_to='student/')
    name = models.CharField(max_length=250, null=True)
    type_of_events = [('tech','tech'), ('soc','soc'), ('spg','spg'), ('stw','stw'), ('ot','ot')]
    type_of_event = models.CharField(max_length=30, default='tech', choices = type_of_events)

    def __str__(self):
        return str(self.category) + str(' | ') + self.name
    