from django.shortcuts import render

def index(request):
    return render(request, 'for1/drivers/drivers.html')

def show_drivers(request,slug):
    context_dict = {}
    
    try:
        driver = Driver.objects.get(slug=slug)
        context_dict['driver'] = driver
        
    except Driver.DoesNotExist:
        context_dict['driver'] = None
        
    return render(request,'for1/drivers/driver.individual.html', context=context_dict)