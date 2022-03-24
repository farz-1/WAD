from django.shortcuts import render
from for1.models import Driver


def index(request):
    context_dict = {}

    try:
        drivers = Driver.objects.all().order_by('overallAverage')
        context_dict['drivers'] = drivers

    except:
        context_dict['drivers'] = None

    return render(request, 'for1/leaderboard/leaderboard.html', context=context_dict)

