import imp
from os import uname
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from numpy import full
from validators import email
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import models  
# Create your views here.
def signup(request):
  
    if request.method == 'POST':  
        print("start1")
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            print("abhay")
            form.save()  
            return HttpResponseRedirect('/profile')
            # message.success(request, 'Account created successfully')  
  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }         
        
    return render(request,"Profile/signup.html",context)



def profile(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return   render(request, 'Profile/Profile.html')

    else:
        return HttpResponseRedirect('/login/')   
def login_page(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            print(user)
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated)
                return HttpResponseRedirect('/profile/')
    return   render(request, 'Profile/login.html',{'form':AuthenticationForm()})  


def logout_page(request):
    logout(request)
    return    HttpResponseRedirect('/login/')

 
def UserProfile(request):
    print(models)
    return HttpResponse("this is it")
