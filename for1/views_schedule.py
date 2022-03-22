from django.shortcuts import render
from for1.models import Race


def index(request):
    races = Race.objects.order_by('-date')
    context_dict = {'races': races}
    return render(request, 'for1/schedule/schedule.html', context=context_dict)