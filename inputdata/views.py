from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
#from .forms import LogInForm
from .models import LogIn,LogInForm
from django.contrib.auth.hashers import make_password,check_password

#def form(request):
#    return render(request,'inputdata/form.html',)

def enterdata(request):
    if request.method=='POST':
        form=LogInForm(request.POST)
        if form.is_valid():
            m=LogIn.objects.all()
            trust=len(m)
            k=LogIn.objects.get(pk=trust)
            k.hash=make_password(k.password)  #manual hashing
            form.save()
            return HttpResponseRedirect('/inputdata/thanks')  #Add  a new link here and in urls.py
    else:
        form=LogInForm()
    return render(request,'inputdata/form.html',{'form':form})  #add template for the form



def thanks(request):
    return render(request,'inputdata/form2.html')

'''
def check(request):
    kk=make_password('Navneel') #works
    rtf=check_password('Navneel',kk) #works
    m="WOW"
    return HttpResponse(rtf) #works
'''
