import imp
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Key
import json
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def search(request):
     
        # else:
        #     context = {
        #         'key': "Home",
        #         'news_res': None,
        #         'starter': ["Hello I'm ABHAY ,Welcome to my website..", "Search the News as your choice..."]
        #     }
 

    # es=response.text.encode('utf-8')

    return render(request, "search/search.html")



def fetch_news(key):
    try:
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"
        headers = {
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
            'x-rapidapi-key': "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
        }
        querystring = {'q': key, "pageNumber": "4", "pageSize": "20", "autoCorrect": "true",
                       "fromPublishedDate": "null", "toPublishedDate": "null"}

   
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        # request for api
        res = json.loads(response.text)
        # print(res)
  
        context = {
            'key':  key,
            'news_res': res['value']
        }
    except:
         context = {
            'key': key,
            'news_res': "no"
        }
    return context



@csrf_exempt
def save_data(request):

    if request.method == "POST":
        b = Key(key=request.POST['key'])
        b.save()
        print(request.POST['key'])
        context=fetch_news(request.POST['key'])
        

        return JsonResponse({'status': context})
    else:
        return JsonResponse({"status": 'fail'})





    #   res=[{

    #         "title":"dkjf ajhg jfa hgjhajg hajdhg jg hajdhg jg hajdhg jad ghjkadhgjd",
    #         "description":"dkjf ajhg jfa hgjhajg haj ajhg jfa hgjhajg haj ajhg jfa hgjhajg hajdhg jad ghjkadhgjd ",
    #         "url":"https://github.com/abhaychhamman ",
    #         "body":"dkjf ajhg jfa hgjhajg hf ajhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhg jad ghjkadhgjd",
    #         "image_url":"img/logo.jpeg",
    #     },
    #     {

    #         "title":"dkjf ajhg jfa hgjhajg hajdhg jg hajdhg jg hajdhg jad ghjkadhgjd",
    #         "description":"dkjf ajhg jfa hgjhajg haj ajhg jfa hgjhajg haj ajhg jfa hgjhajg hajdhg jad ghjkadhgjd ",
    #         "url":"https://github.com/abhaychhamman ",
    #         "body":"dkjf ajhg jfa hgjhajg hf ajhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhjhg jfa hgjhajg hajdhg jad ghjkadhgjd",
    #         "image_url":"img/logo.jpeg",
    #     }
    #     ]