from django.db import models
from django.forms import ModelForm

class LogIn(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)

class LogInForm(ModelForm):
    class Meta:
        model=LogIn
        fields="__all__"
