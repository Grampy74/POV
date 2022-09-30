from django.shortcuts import render
from newsapi import NewsApiClient

def news(request):

    newsapi = NewsApiClient(api_key='f56f170cef0c4bc3b8ffa3ad05c070bb')
    top = newsapi.get_top_headlines(sources='cnn')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'news.html', context={"mylist":mylist})