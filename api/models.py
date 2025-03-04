from django.db import models

# Create your models here.

STATE_CHOICE = ((
    ('Bihar','Bihar'),
    ('Jharkhand','Jharkhand'),
    ('Maharashtra','Maharashtra'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Delhi','Delhi'),
    ('Rajasthan','Rajasthan'),
    ('Tamil Nadu','Tamil Nadu'),
))


class Profile(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    dob = models.DateField(auto_now = False, auto_now_add = False)
    state = models.CharField(choices = STATE_CHOICE,max_length=50)
    gender = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    pimage = models.ImageField(upload_to= 'pimages', blank = True)
    rdoc = models.FileField(upload_to= 'rdocs', blank = True)