from django.shortcuts import render

def index(request):
    return render(request, 'for1/profile/profile.html', {'user': request.user})