from os import uname
from django.http import HttpResponse
from django.shortcuts import redirect, render
from numpy import full
from validators import email
from .models import Profile
# Create your views here.
def signup(request):
    fname=request.GET.get('fullname')
    em=request.GET.get('email')
    passw=request.GET.get('pass')
    cpassw=request.GET.get('cpass')
    uname=request.GET.get('username')
    submit=request.GET.get('signup')
    print(submit ,uname)
    if submit=="Signup" :
        try:
            
            
            user_name_exist = Profile.objects.get(username=uname)
            context={'message':'Already UserName Exists! .Please Login Your Account!'}
            return   render(request,"Profile/login.html",context)
        except:
            if  passw==cpassw  :
                b = Profile(fullname=fname,email=em,password=passw,username=uname)
                b.save() 
                print("data added")
                return   render(request,"Profile/Profile.html")
            
        
    return render(request,"Profile/signup.html")

    
def profile(request):
  
    return render(request,"Profile/Profile.html")
    
def login(request):
    return render(request,"Profile/login.html")

 
    
    