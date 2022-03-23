from django.shortcuts import render

def index(request):
    return render(request, 'for1/cars/car.rating_form.html', context=context_dict)