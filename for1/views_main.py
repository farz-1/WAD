from django.shortcuts import render, redirect


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'for1/home/home.html')