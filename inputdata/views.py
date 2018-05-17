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
            #current_form=form.objects.get(id=1)
            #current_form.hashpass=make_password(current_form.password)
            form.save()
            return HttpResponseRedirect('/inputdata/thanks')  #Add  a new link here and in urls.py
    else:
        form=LogInForm()
    return render(request,'inputdata/form.html',{'form':form})  #add template for the form



def thanks(request):
    return render(request,'inputdata/form2.html')
