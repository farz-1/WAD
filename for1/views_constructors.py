from django.shortcuts import render
from for1.models import Constructor


def index(request):
    context_dict = {}

    try:
        constructors = Constructor.objects.all()
        context_dict['constructors'] = constructors

    except:
        context_dict['constructors'] = None

    return render(request, 'for1/constructors/constructors.html', context=context_dict)


def constructor_details(request, slug):
    context_dict = {}

    try:
        constructor = Constructor.objects.get(slug=slug)
        context_dict['constructor'] = constructor

    except Constructor.DoesNotExist:
        context_dict['constructor'] = None

    return render(request, 'for1/constructors/constructor.individual.html', context=context_dict)
