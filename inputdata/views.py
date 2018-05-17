from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import LogInForm
from .models import LogIn,LogInForm

#def form(request):
#    return render(request,'inputdata/form.html',)

def enterdata(request):
    if request.method=='POST':
        form=LogInForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inputdata')  #Add the link here and in urls.py
    else:
        form=LogInForm()
    return render(request,'inputdata/form.html',{'form':form,})  #add template for the form

# Create your views here.
