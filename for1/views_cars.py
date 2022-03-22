from django.shortcuts import render
from for1.models import Car


def index(request):
    context_dict = {}

    try:
        cars = Car.objects.all()
        context_dict['cars'] = cars

    except:
        context_dict['cars'] = None

    return render(request, 'for1/cars/cars.html', context=context_dict)


def car_details(request, slug):
    context_dict = {}

    try:
        car = Car.objects.get(slug=slug)
        context_dict['car'] = car

    except Car.DoesNotExist:
        context_dict['car'] = None

    return render(request, 'for1/cars/cars.individual.html', context=context_dict)