# code by me 

import imp
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
 

def index(request):
    

# ******************* trending news **************************

    import json
    import requests

    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI"

    querystring = {"pageNumber":"1","pageSize":"50","withThumbnails":"false","location":"india"}

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

# # print(type(response.text.encode('utf-8')))
    es=response.text.encode('utf-8')
    res = json.loads(es)
    # [u'totalCount', u'_type', u'relatedSearch', u'value', u'didUMean']
    # print(50*"-")
    # print(res['value'][0]['body'])
    # print(50*"-")
    # print(res['value'][0]['description'])
    # print(50*"-")
    # print(res['value'][0]['title'])
    # print(50*"-")
    # print(res['value'][0]['language'])
    # print(50*"-")
    # print("this is image",res['value'][0]['image'])
    # print(50*"-")
    # print(res['value'][0]['datePublished'])
    # print(50*"-")
    # print(res['value'][0]['snippet'])
    # print(50*"-")
    # print(res['value'][0]['isSafe'])
    # print(50*"-")
    # print(res['value'][0]['provider'])
    # print(50*"-")
    # print(res['value'][0]['id'])
    # print(50*"-")
    # print(res['value'][0]['keywords'])
    # print(50*"-")
    # print(type(res['value'][0]))
    
    # [u'body', u'description', u'language', u'title', u'url', u'image', u'datePublished', u'snippet', u'isSafe', u'provider', u'keywords', u'id']
    # params={'body':res['value'][0]['body'],'description':res['value'][0]['description'],'title':res['value'][0]['title'],'url':res['value'][0]['url'],'image_url':res['value'][0]['image']['url'],'body':res['value'][0]['body'],'body':res['value'][0]['body'],'datePublished':res['value'][0]['datePublished'],'analyzed_text':'this is all right'}
    params={'items':res['value']}
    return render(request,"analyze.html",params)
    
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
 