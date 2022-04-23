from os import uname
from django.http import HttpResponse
from django.shortcuts import redirect, render
from numpy import full
from validators import email
from .models import Profile
# Create your views here.
def profile(request):
    fname=request.GET.get('fullname')
    em=request.GET.get('email')
    passw=request.GET.get('pass')
    cpassw=request.GET.get('cpass')
    uname=request.GET.get('username')
    submit=request.GET.get('signup')
    
    if submit=="Signup" :
        try:
            
            
            user_name_exist = Profile.objects.get(username=uname)
            return HttpResponse("username already exists!")  
        except:
            if  passw==cpassw  :
                b = Profile(fullname=fname,email=em,password=passw,username=uname)
                b.save() 
                print("data added")
                return HttpResponse("You have signup Successfully!")
            
        
    return render(request,"Profile/Profile.html")

    
    

 
    
    