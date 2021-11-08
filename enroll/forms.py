from django.core import validators
from django import forms
from .models import User

class Student(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels ={'name':'Enter Your Name', 'email': 'Enter Your Email', 'password': 'Enter Your Password'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),'email': forms.EmailInput(attrs={'class': 'form-control'}),'password': forms.PasswordInput(attrs={'class': 'form-control'}),  }
        
        