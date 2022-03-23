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


def details(request, slug):
    context_dict = {}
    
    try:
        driver = Driver.objects.get(slug=slug)
        context_dict['driver'] = driver
        
    except Driver.DoesNotExist:
        context_dict['driver'] = None
        
    return render(request, 'for1/drivers/driver.details.html', context=context_dict)

def rate(request, slug):
    context_dict = {}
    if request.method == 'POST':
        print(request.POST)
        print('RATE WITH POST')
        rating_form = DriverRatingForm(request.POST)
        context_dict['rating_form'] = rating_form

        print("XXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxXx\n\n")
        print(rating_form.errors.as_data())
        print("XXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxXx\n\n")
        print(rating_form)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            print(rating)
            rating.userID = request.user
            rating.carID = drivers.objects.get(slug=slug)
            rating.save()

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
            drivers = drivers.objects.get(slug=slug)
            context_dict['drivers'] = drivers

        except Driver.DoesNotExist:
            context_dict['drivers'] = None

        return render(request, 'for1/drivers/driver.rating_form.html', context=context_dict)