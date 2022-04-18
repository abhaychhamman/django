
from tkinter import NO
from django.shortcuts import render
from matplotlib.pyplot import title
import wikipedia
from django.http import HttpResponse
import pyautogui as pg 
import time


  

def index(request):
    
    totalques=request.GET.get('totalques')

    if totalques==None:
        print("abhay")
        totalques="abhay".split(" ")
    mkpdf=request.GET.get('pdf')
    next=request.GET.get('next')
  
    combine=[]
    for i in range(len(totalques)-1):
        answer=wikipedia.summary(totalques[i], sentences = 30).split(".")
       
        
        combine.append({"question":totalques[i],"answer":answer[:-1]})
        # combine=[{'question':"abhay",'answer':'akjdkgjkjajg'},{'question':"abhay",'answer':'akjdkgjkjajg'}]
    
    print(mkpdf)
    if mkpdf=="Make Pdf":
        pg.hotkey("ctrl","p")
        time.sleep(2)
        pg.click(1135,713)
        pg.click(611,50)
        pg.hotkey("ctrl","a")
        time.sleep(1)
        pg.typewrite("abhay.pdf")
        pg.sleep(1)
        pg.click(1231,43)
        pg.click(1231,43)
   
 
      
    context={
 
        'combine':combine,
         
    }
    return render(request,"topic/topic.html",context)


 