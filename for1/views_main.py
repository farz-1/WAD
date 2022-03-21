from django.shortcuts import render, redirect
from django.http import HttpResponse
from for1.forms import UserForm, UserProfileForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'for1/home.html')


def about(request):
    return render(request, 'for1/about.html')


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

            send_mail(
                subject='F1 Rating App Sign-Up',
                message='Thank you very much for signing up to our application! Have fun rating some F1 drivers, cars and constructors!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('index')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'for1/users/user.register.html',
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

    return render(request, 'for1/users/user.login.html')