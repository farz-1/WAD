from django.shortcuts import render

def index(request):
    return render(request, 'for1/leaderboard/leaderboard.html', context=context_dict)