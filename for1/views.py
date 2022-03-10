from pickle import TRUE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from for1.forms import UserForm, UserProfileForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'for1/index.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            return redirect('index')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'for1/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form})


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')

            else:
                HttpResponse("Account disabled. Please re-verify your account.")

        else:
            print("Invalid login details.")

    return render(request, 'for1/login.html')
