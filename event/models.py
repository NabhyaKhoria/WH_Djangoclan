from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='technology/')
    description = models.TextField(null=True)
    types = [('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'),
             ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')]
    month_of_event = models.CharField(
        max_length=30, default='Jan', choices=types)
    date = models.DateField(null=True)
    type_of_events = [('soon', 'soon'), ('att', 'att'), ('imp', 'imp')]
    type_of_event = models.CharField(
        max_length=30, default='soon', choices=type_of_events)

    day_of_events = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                     ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]
    day_of_event = models.CharField(
        max_length=30, default='Monday', choices=day_of_events)

    deadline = models.DateTimeField(auto_now_add=True, null=True)
    SuperviserName = models.CharField(max_length=50, null=True)
    SuperviserEmail = models.CharField(max_length=60, null=True)
    SuperviserContact = models.CharField(max_length=30, null=True)

    VenueName = models.CharField(max_length=60, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class StudentWelfare(models.Model):
    name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='technology/')
    description = models.TextField(null=True)
    types = [('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'),
             ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')]
    month_of_event = models.CharField(
        max_length=30, default='Jan', choices=types)
    date = models.DateField(null=True)
    type_of_events = [('soon', 'soon'), ('att', 'att'), ('imp', 'imp')]
    type_of_event = models.CharField(
        max_length=30, default='soon', choices=type_of_events)

    day_of_events = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), (
        'Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]
    day_of_event = models.CharField(
        max_length=30, default='Monday', choices=day_of_events)

    deadline = models.DateTimeField(auto_now_add=True, null=True)
    SuperviserName = models.CharField(max_length=50, null=True)
    SuperviserEmail = models.CharField(max_length=60, null=True)
    SuperviserContact = models.CharField(max_length=30, null=True)

    VenueName = models.CharField(max_length=60, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='technology/')
    description = models.TextField(null=True)
    types = [('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'),
             ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')]
    month_of_event = models.CharField(
        max_length=30, default='Jan', choices=types)
    date = models.DateField(null=True)
    type_of_events = [('soon', 'soon'), ('att', 'att'), ('imp', 'imp')]
    type_of_event = models.CharField(
        max_length=30, default='soon', choices=type_of_events)

    day_of_events = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), (
        'Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]
    day_of_event = models.CharField(
        max_length=30, default='Monday', choices=day_of_events)

    deadline = models.DateTimeField(auto_now_add=True, null=True)
    SuperviserName = models.CharField(max_length=50, null=True)
    SuperviserEmail = models.CharField(max_length=60, null=True)
    SuperviserContact = models.CharField(max_length=30, null=True)

    VenueName = models.CharField(max_length=60, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Sports(models.Model):
    name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=70)
    image = models.ImageField(upload_to='technology/')
    description = models.TextField(null=True)
    types = [('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'),
             ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')]
    month_of_event = models.CharField(
        max_length=30, default='Jan', choices=types)
    date = models.DateField(null=True)
    type_of_events = [('soon', 'soon'), ('att', 'att'), ('imp', 'imp')]
    type_of_event = models.CharField(
        max_length=30, default='soon', choices=type_of_events)

    day_of_events = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), (
        'Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]
    day_of_event = models.CharField(
        max_length=30, default='Monday', choices=day_of_events)

    deadline = models.DateTimeField(auto_now_add=True, null=True)
    SuperviserName = models.CharField(max_length=50, null=True)
    SuperviserEmail = models.CharField(max_length=60, null=True)
    SuperviserContact = models.CharField(max_length=30, null=True)

    VenueName = models.CharField(max_length=60, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class resultss(models.Model):
    name = models.CharField(max_length=50)
    gold = models.CharField(max_length=100)
    silver = models.CharField(max_length=100)
    bronze = models.CharField(max_length=100)

    def __str__(self):
        return self.name
