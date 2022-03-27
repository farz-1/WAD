import os

from django.shortcuts import render, redirect
from for1.forms import UserProfileForm, UserProfile, UserForm, UserProfilePictureForm
from for1.models import Constructor, Driver, Car, CarRating, DriverRating, ConstructorRating
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth
from django.contrib import messages


def index(request):
    context_dict = {}

    try:
        user_profile = UserProfile.objects.get(user=request.user)
        context_dict['user'] = request.user
        context_dict['user_profile'] = user_profile

        car_ratings = CarRating.objects.all().filter(userID=request.user)
        context_dict['car_ratings'] = car_ratings

        driver_ratings = DriverRating.objects.all().filter(userID=request.user)
        context_dict['driver_ratings'] = driver_ratings

        constructor_ratings = ConstructorRating.objects.all().filter(userID=request.user)
        context_dict['constructor_ratings'] = constructor_ratings

        profile_picture = str(settings.MEDIA_URL) + str(user_profile.picture)
        context_dict['profile_picture'] = profile_picture

    except:
        context_dict['user'] = None
        context_dict['user_profile'] = None

    return render(request, 'for1/users/user.profile.html', context=context_dict)


def edit(request):
    context_dict = {}
    context_dict['constructors'] = Constructor.objects.all()
    context_dict['drivers'] = Driver.objects.all()
    context_dict['cars'] = Car.objects.all()

    try:
        user_profile = UserProfile.objects.get(user=request.user)
        context_dict['user_profile'] = user_profile

    except user_profile.DoesNotExist:
        context_dict['user_profile'] = None

    try:
        profile_edit_form = UserProfileForm(instance=user_profile, data=request.POST)
        context_dict['profile_edit_form'] = profile_edit_form


    except profile_edit_form.DoesNotExist:
        context_dict['profile_edit_form'] = None

    if request.method == 'POST':
        picture_form = UserProfileForm(instance=user_profile, data=request.POST)

        if profile_edit_form.is_valid() and picture_form.is_valid():
            saved_form = profile_edit_form.save()

            if 'picture' in request.FILES:
                if user_profile.picture != 'profile_images/default.jpg':
                    os.remove(user_profile.picture.path)

                profile = picture_form.save(commit=False)
                profile.picture = request.FILES['picture']
                profile.save()
            saved_form.save()
            messages.success(request, "Profile edited successfully")
            return redirect('profile')

        else:
            messages.error(request, "Profile could not be edited. Please try again")
            return redirect('profile_edit')

    return render(request, 'for1/users/user.profile.edit.html', context=context_dict)



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