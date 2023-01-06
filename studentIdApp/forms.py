from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . import models




class SignUp(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')

class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')