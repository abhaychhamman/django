import requests
import json

url = "https://instagram47.p.rapidapi.com/get_stories"

headers = {
    'x-rapidapi-host': "instagram47.p.rapidapi.com",
    'x-rapidapi-key': "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
    }

response = requests.request("GET", 'https://randomuser.me/api/', )
a=response.text.encode('utf-8').replace("{","").replace("}","")
b=a.split(",")
for j in b:
	print(j)

res = json.loads(a)
print(res)