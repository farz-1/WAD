from django.shortcuts import render
from for1.models import News


def index(request):
    news = News.objects.order_by('-published')[:10]
    context_dict = {}
    context_dict['news'] = news
    return render(request, 'for1/news/news.html', context=context_dict)
