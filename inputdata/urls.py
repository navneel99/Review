from django.urls import path
from . import views

urlpatterns = [
    path('',views.enterdata, name="form" ),
    path('thanks',views.thanks, name="thanks" ),


]
