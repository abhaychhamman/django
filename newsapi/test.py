from newsapi import NewsApiClient
from numpy import source
import requests
 
newsapi = NewsApiClient(api_key='5b817388356c468b96ffce430d2aca72')
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news',
#                                           category='business',
#                                           language='en',
#                                           country='india')
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
sources = newsapi.get_sources()['sources']
# print(sources)
# print(sources[0].keys())
for name in range(len(sources)):
    print( sources)

# print(sources[0]['name'])