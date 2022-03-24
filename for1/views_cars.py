from django.db.models import Avg
from django.shortcuts import render, redirect
from for1.models import Car, CarRating
from for1.forms import CarRatingForm
from django.contrib import messages


def index(request):
    context_dict = {}

    try:
        cars = Car.objects.all()
        context_dict['cars'] = cars

    except:
        context_dict['cars'] = None

    return render(request, 'for1/cars/cars.html', context=context_dict)


def details(request, slug):
    context_dict = {}

    try:
        car = Car.objects.get(slug=slug)
        context_dict['car'] = car

    except Car.DoesNotExist:
        context_dict['car'] = None

    return render(request, 'for1/cars/cars.details.html', context=context_dict)


def rate(request, slug):
    if request.user.is_anonymous:
        return redirect('profile')

    context_dict = {}
    if request.method == 'POST':
        rating_form = CarRatingForm(request.POST)
        context_dict['rating_form'] = rating_form

        if rating_form.is_valid():
            userID = request.user
            carID = Car.objects.get(slug=slug)

            if CarRating.objects.filter(userID=userID, carID=carID).exists():
                data = request.POST.dict()
                rating = CarRating.objects.get(userID=userID, carID=carID)
                data.pop('csrfmiddlewaretoken')

                for k, v in data.items():
                    setattr(rating, k, int(v))

            else:
                rating = rating_form.save(commit=False)
                rating.userID = userID
                rating.carID = carID

            rating.save()

            update = Car.objects.get(model=carID.model)
            carSet = CarRating.objects.filter(carID=carID)
            update.overallAverage = carSet.aggregate(Avg('overallAverage'))['overallAverage__avg']

            update.save()
            messages.success(request, "Rating submitted successfully")
            return redirect('cars')

        else:
            messages.error(request, "Rating could not be submitted. Please try again")
            return redirect('car_rate', slug)

    else:
        context_dict = {}
        rating_form = CarRatingForm()
        context_dict['rating_form'] = rating_form

        try:
            car = Car.objects.get(slug=slug)
            context_dict['car'] = car

        except Car.DoesNotExist:
            context_dict['car'] = None

        return render(request, 'for1/cars/car.rating_form.html', context=context_dict)