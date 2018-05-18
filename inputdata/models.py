from django.db import models
from django.forms import ModelForm, widgets
from django import forms

class LogIn(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    hash=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class LogInForm(ModelForm):

    class Meta:
        password=forms.CharField(widget=forms.PasswordInput(),max_length=30)
        model=LogIn
        fields=['username','password']
