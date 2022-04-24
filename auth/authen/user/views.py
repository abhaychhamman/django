from email import message
from django.http import HttpResponseRedirect
 
from django.shortcuts import render  
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
# Create your views here.  
  
def register(request):  
 
    if request.method == 'POST':  
        print("start1")
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            print("abhay")
            form.save()  
            return render(request, 'user/profile.html')
            # message.success(request, 'Account created successfully')  
  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'user/user.html', context)  

def profile(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return   render(request, 'user/profile.html')

    else:
        return HttpResponseRedirect('/login/')   
def login_page(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated)
                return HttpResponseRedirect('/profile/')
    return   render(request, 'user/login.html',{'form':AuthenticationForm()})  


# def logout_page(request):
#     logout(request)
#     return    HttpResponseRedirect('/login/')