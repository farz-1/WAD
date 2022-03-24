from django.db.models import Avg
from django.shortcuts import render, redirect
from for1.models import Driver, DriverRating
from for1.forms import DriverRatingForm
from django.contrib import messages


def index(request):
    context_dict = {}

    try:
        drivers = Driver.objects.all()
        context_dict['drivers'] = drivers

    except:
        context_dict['drivers'] = None

    return render(request, 'for1/drivers/drivers.html', context=context_dict)


def details(request, slug):
    context_dict = {}

    try:
        driver = Driver.objects.get(slug=slug)
        context_dict['driver'] = driver

    except Driver.DoesNotExist:
        context_dict['driver'] = None

    return render(request, 'for1/drivers/driver.details.html', context=context_dict)


def rate(request, slug):
    if request.user.is_anonymous:
        return redirect('profile')

    context_dict = {}

    if request.method == 'POST':
        rating_form = DriverRatingForm(request.POST)
        context_dict['rating_form'] = rating_form

        if rating_form.is_valid():
            userID = request.user
            driverID = Driver.objects.get(slug=slug)
            data = request.POST.dict()

            if DriverRating.objects.filter(userID=userID, driverID=driverID).exists():
                rating = DriverRating.objects.get(userID=userID, driverID=driverID)
                data.pop('csrfmiddlewaretoken')

                for k, v in data.items():
                    setattr(rating, k, int(v))

            else:
                rating = rating_form.save(commit=False)
                rating.userID = userID
                rating.driverID = driverID

            rating.save()

            update = Driver.objects.get(name=driverID.name)
            driverSet = DriverRating.objects.filter(driverID=driverID)
            update.overallAverage = driverSet.aggregate(Avg('overallAverage'))['overallAverage__avg']

            update.save()
            messages.success(request, "Rating submitted successfully")
            return redirect('drivers')

        else:
            messages.error(request, "Rating could not be submitted. Please try again")
            return redirect('driver_rate', slug)

    else:
        context_dict = {}
        rating_form = DriverRatingForm()
        context_dict['rating_form'] = rating_form

        try:
            driver = Driver.objects.get(slug=slug)
            context_dict['driver'] = driver

        except Driver.DoesNotExist:
            context_dict['driver'] = None

        return render(request, 'for1/drivers/driver.rating_form.html', context=context_dict)