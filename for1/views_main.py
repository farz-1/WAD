from django.shortcuts import render, redirect
from for1.forms import UserForm, UserProfilePictureForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth
from django.contrib import messages


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'for1/home/home.html')


def about(request):
    return render(request, 'for1/about.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfilePictureForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            else:
                profile.picture = 'profile_images/default.jpg'
            profile.save()

            send_mail(
                subject='F1 Rating App Sign-Up',
                message='Thank you very much for signing up to our application! Have fun rating some F1 drivers, cars and constructors!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            messages.success(request, "Account successfully created")
            return redirect('login')

        else:
            messages.error(request, "Creation of the account unsuccessful. Please try again")

    else:
        user_form = UserForm()
        profile_form = UserProfilePictureForm()

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
                messages.success(request, "Successfully logged in")
                return redirect('index')

            else:
                messages.error(request, "Account disabled. Please re-verify your account.")

        else:
            messages.error(request, "Invalid login details.")

    return render(request, 'for1/users/user.login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')