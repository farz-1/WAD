from django.shortcuts import render
from for1.models import Driver, Car, Constructor


def index_driver(request):
    context_dict = {}

    try:
        drivers = Driver.objects.all().order_by('-overallAverage')
        context_dict['drivers'] = drivers

    except:
        context_dict['drivers'] = None

    return render(request, 'for1/leaderboard/leaderboard.driver.html', context=context_dict)


def index_car(request):
    context_dict = {}

    try:
        cars = Car.objects.all().order_by('-overallAverage')
        context_dict['cars'] = cars

    except:
        context_dict['cars'] = None

    return render(request, 'for1/leaderboard/leaderboard.car.html', context=context_dict)


def index_constructor(request):
    context_dict = {}

    try:
        constructors = Constructor.objects.all().order_by('-overallAverage')
        context_dict['constructors'] = constructors

    except:
        context_dict['constructors'] = None

    return render(request, 'for1/leaderboard/leaderboard.constructor.html', context=context_dict)