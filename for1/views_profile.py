from django.shortcuts import render

def index(request):
    return render(request, 'for1/users/user.profile.html', {'user': request.user})