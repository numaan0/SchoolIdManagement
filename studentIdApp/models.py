from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from functools import partial

# Create your models here.


class User(AbstractUser):
    schoolname=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.username

roleChoices=(
        ("Teacher","Teacher"),
        ("Student","Student")
    )    
class Student(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fullname= models.CharField(max_length=50)
    father = models.CharField(max_length=30)
    mother = models.CharField(max_length=30)
    phno=models.IntegerField()
    ephno = models.IntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=100)
    photo= models.ImageField(upload_to='photos/', default='photos/default.png')
    role=models.CharField(max_length=20,choices=roleChoices)
    rollNumber = models.IntegerField()
    standard = models.CharField( max_length=10)
    
    def __str__(self):
        return self.fullname
  
class Teacher(models.Model):
    usert = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fullname= models.CharField(max_length=50)
    father = models.CharField(max_length=30)
    mother = models.CharField(max_length=30)
    phno=models.IntegerField()
    ephno = models.IntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=100)
    photo= models.ImageField(upload_to="photos/", default='photos/default.png')
    role=models.CharField(max_length=20,choices=roleChoices)
    
    def __str__(self):
        return self.fullname   
