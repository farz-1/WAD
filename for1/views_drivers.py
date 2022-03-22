from django.shortcuts import render
from for1.models import Driver


def index(request):
    context_dict = {}

    try:
        drivers = Driver.objects.all()
        context_dict['drivers'] = drivers

    except:
        context_dict['drivers'] = None

    return render(request, 'for1/drivers/drivers.html', context=context_dict)


def driver_details(request, slug):
    context_dict = {}
    
    try:
        driver = Driver.objects.get(slug=slug)
        context_dict['driver'] = driver
        
    except Driver.DoesNotExist:
        context_dict['driver'] = None
        
    return render(request, 'for1/drivers/driver.individual.html', context=context_dict)