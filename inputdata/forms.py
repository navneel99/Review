'''from django import forms
from django.forms import widgets

class LogInForm(forms.Form):
    """docstring for LogInForm.forms.Formef __init__(self, arg):
        super(LogInForm,forms.Form.__init__()
        self.arg = arg"""
    user_name=forms.CharField(label="username",max_length=40)
    password=forms.CharField(label="password") #Change it to password
'''
