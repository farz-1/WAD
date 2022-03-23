from django.shortcuts import render

def ratings(request):
    return render(request, 'for1/cars/car.rating_form.html')