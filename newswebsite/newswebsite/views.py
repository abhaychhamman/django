import imp
from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
  
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
    params={'items':res['value']}
    return  render(request,'analyze.html',params)
    # return HttpResponse("this is abhay kumar singh")
