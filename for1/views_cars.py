from django.shortcuts import render

def index(request):
    return render(request, 'for1/cars/cars.html')

def rate(request, id):
    return render(request, 'for1/cars/car.rating_form.html')
