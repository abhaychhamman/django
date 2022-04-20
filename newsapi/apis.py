 
from webbrowser import get
import requests
import json



url = "https://quotes15.p.rapidapi.com/quotes/random"

# https://v2.jokeapi.dev/joke/Any?amount=20
# url = " https://cricket-api.vercel.app/cri.php?url=https://www.cricbuzz.com/live-cricket-scores/46011/"

# url = "https://meme-api.herokuapp.com/gimme/wholesomememes/150"

# url = "https://cricket-live-data.p.rapidapi.com/series"

# url = "https://cricket-live-data.p.rapidapi.com/match/2432999"

# url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/AutoComplete"

# url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"
# url = f"https://newsapi.org/v2/everything?q={query}&from=2022-03-15&sortBy=publishedAt&apiKey=5b817388356c468b96ffce430d2aca72"

# url = "https://cricket-live-data.p.rapidapi.com/match/2432999"
 
# url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
 
# querystring = {"pageNumber":"1","pageSize":"20","withThumbnails":"false","location":"delhi",format:json}

# headers = {
#     'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
#     'x-rapidapi-key': "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
#     }
  
# # ******************


# response = requests.request("GET", url,headers=headers)
# res = json.loads(response.text)
 
# print(res)
 


# import requests

# url = "https://quotes15.p.rapidapi.com/quotes/random/"

# headers = {
# 	"X-RapidAPI-Host": "quotes15.p.rapidapi.com",
# 	"X-RapidAPI-Key": "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)






 
import requests

# url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
	"X-RapidAPI-Key": "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
}

response = requests.request("GET", url, headers=headers)

print(response.text)