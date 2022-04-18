import requests	
sources="bbc-news"
query_params = {

	"source": sources,
	"sortBy": "all",
	"apiKey": "5b817388356c468b96ffce430d2aca72"
	}
main_url = " https://newsapi.org/v1/articles"
res = requests.get(main_url, params=query_params)
open_bbc_page = res.json()
print(open_bbc_page)
# article = open_bbc_page["articles"]
 