from pickle import TRUE
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'for1/cars/cars.html')

def ratings(request):
    return render(request, 'for1/cars/car.ratings.html')