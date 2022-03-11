from django.shortcuts import render

def index(request):
    return render(request, 'for1/news/news.html')