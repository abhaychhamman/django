# code by me 

import imp
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
 

def index(request):
    # return HttpResponse("<h1>abhay</h1> kumar isngh ")
    return render(request,"analyze.html")
    
def analyze(request):
    # get the text
    djtext =request.GET.get('text','default')
    removepunc =request.GET.get('removepunc','off')
    print(djtext)
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_-'''
    analyze_txt=""
    if removepunc=='on':

        for char in djtext:
            if char not in punctuations:
                analyze_txt=analyze_txt+char
    else:
        analyze_txt=djtext
    # here definne dictionary for parameter
    params={'purpose':'Removed Punctuations','analyzed_text':analyze_txt}
    return  render(request,'analyze.html',params)


# here define pipeline

# def capitalizefirst(request):
#     return HttpResponse("<h1>hi guys , i am capitalizefirst leone </h1> kumar isngh ")
# def newlineremove(request):
#     return HttpResponse("<h1>hi guys , i am newlineremove leone </h1> kumar isngh ")
# def spaceremove(request):
#     return HttpResponse("<h1>hi guys , i am spaceremove leone </h1> kumar isngh ")
# def charcount(request):
#     return HttpResponse("<h1>hi guys , i am charcount leone </h1> kumar isngh ")
 