from django.db.models import Avg
from django.shortcuts import render, redirect
from for1.models import Constructor, ConstructorRating
from for1.forms import ConstructorRatingForm
from django.contrib import messages


def index(request):
    context_dict = {}

    try:
        constructors = Constructor.objects.all()
        context_dict['constructors'] = constructors

    except:
        context_dict['constructors'] = None

    return render(request, 'for1/constructors/constructors.html', context=context_dict)


def leaderboard(request):
    context_dict = {}

    try:
        constructors = Constructor.objects.all().order_by('-overallAverage')
        context_dict['constructors'] = constructors

    except:
        context_dict['constructors'] = None

    return render(request, 'for1/constructors/constructors.leaderboard.html', context=context_dict)


def details(request, slug):
    context_dict = {}

    try:
        constructor = Constructor.objects.get(slug=slug)
        context_dict['constructor'] = constructor

    except Constructor.DoesNotExist:
        context_dict['constructor'] = None

    return render(request, 'for1/constructors/constructor.details.html', context=context_dict)


def rate(request, slug):
    if request.user.is_anonymous:
        return redirect('profile')

    context_dict = {}

    if request.method == 'POST':
        rating_form = ConstructorRatingForm(request.POST)
        context_dict['rating_form'] = rating_form

        if rating_form.is_valid():
            userID = request.user
            constructorID = Constructor.objects.get(slug=slug)

            if ConstructorRating.objects.filter(userID=userID, constructorID=constructorID).exists():
                data = request.POST.dict()
                rating = ConstructorRating.objects.get(userID=userID, constructorID=constructorID)
                data.pop('csrfmiddlewaretoken')

                for k, v in data.items():
                    setattr(rating, k, int(v))

            else:
                rating = rating_form.save(commit=False)
                rating.userID = userID
                rating.constructorID = constructorID

            rating.save()

            update = Constructor.objects.get(name=constructorID.name)
            constructorSet = ConstructorRating.objects.filter(constructorID=constructorID)
            update.overallAverage = constructorSet.aggregate(Avg('overallAverage'))['overallAverage__avg']

            update.save()
            messages.success(request, "Rating submitted successfully")
            return redirect('constructors')

        else:
            messages.error(request, "Rating could not be submitted. Please try again")
            return redirect('constructor_rate', slug)

    else:
        context_dict = {}
        rating_form = ConstructorRatingForm()
        context_dict['rating_form'] = rating_form

        try:
            constructor = Constructor.objects.get(slug=slug)
            context_dict['constructor'] = constructor

        except Constructor.DoesNotExist:
            context_dict['constructor'] = None

        return render(request, 'for1/constructors/constructor.rating_form.html', context=context_dict)