from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='technology/')
    description = models.TextField(null=True)
    types = [('Jan','Jan'), ('Feb','Feb'), ('Mar','Mar'),('Apr','Apr'), ('May','May'), ('Jun','Jun'),('Jul','Jul'), ('Aug','Aug'), ('Sep','Sep'),('Oct','Oct'), ('Nov','Nov'), ('Dec','Dec')]
    month_of_event = models.CharField(max_length=30, default='Jan', choices = types)
    date = models.IntegerField(default=0,validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ])
    type_of_events = [('soon','soon'), ('att','att'), ('imp','imp')]
    type_of_event = models.CharField(max_length=30, default='soon', choices = type_of_events)

    def __str__(self):
        return self.name