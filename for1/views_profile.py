import os

from django.shortcuts import render, redirect
from for1.forms import UserProfileForm, UserProfile
from django.contrib import messages
from for1.models import Constructor, Driver, Car, CarRating, DriverRating, ConstructorRating
from django.conf import settings


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

    return render(request, 'for1/profile/profile.html', context=context_dict)


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

    return render(request, 'for1/profile/profile.edit.html', context=context_dict)