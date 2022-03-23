from django.shortcuts import render, redirect
from pyexpat.errors import messages

from for1.forms import ConstructorRatingForm
from for1.models import Constructor, Driver


def index(request):
    context_dict = {}

    try:
        constructors = Constructor.objects.all()
        context_dict['constructors'] = constructors

    except:
        context_dict['constructors'] = None

    return render(request, 'for1/constructors/constructors.html', context=context_dict)


def details(request, slug):
    context_dict = {}

    try:
        constructor = Constructor.objects.get(slug=slug)
        context_dict['constructor'] = constructor

        drivers = Driver.objects.filter(constructor=constructor.name)
        context_dict['drivers'] = drivers

    except Constructor.DoesNotExist:
        context_dict['constructor'] = None

    return render(request, 'for1/constructors/constructor.details.html', context=context_dict)


def rate(request, slug):
    context_dict = {}
    if request.method == 'POST':
        print(request.POST)
        print('RATE WITH POST')
        rating_form =ConstructorRatingForm(request.POST)
        context_dict['rating_form'] = rating_form

        print("XXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxXx\n\n")
        print(rating_form.errors.as_data())
        print("XXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxXx\n\n")
        print(rating_form)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            print(rating)
            rating.userID = request.user
            rating.conID=Constructor.objects.get(slug=slug)
            rating.save()
            messages.success(request, "Rating submitted successfully")
            return redirect('constructors')
        else:
            messages.error(request, "Rating could not be submitted. Please try again")
            return redirect('constructor_rate', slug)
    else:
        context_dict = {}
        rating_form=ConstructorRatingForm()
        context_dict['rating_form'] = rating_form
        try:
            constructor = Constructor.objects.get(slug=slug)
            context_dict['constructor'] = constructor

        except Constructor.DoesNotExist:
            context_dict['constructor'] = None
    return render(request, 'for1/constructors/constructor.rating_form.html.html', context=context_dict)
