from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]

# Create your models here.
class Student(User):
    Email_address=models.EmailField(blank=False,unique=True)
    middlename=models.CharField(max_length=20,blank=True)
    dob=models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    mob=models.IntegerField(unique=True)
    city=models.CharField(max_length=20)
    pin=models.IntegerField()