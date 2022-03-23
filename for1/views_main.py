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

        print(request.POST)
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
            profile.save()

            send_mail(
                subject='F1 Rating App Sign-Up',
                message='Thank you very much for signing up to our application! Have fun rating some F1 drivers, cars and constructors!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            messages.success(request, f"Account successfully created {user.username}")
            messages.success(request, f"You are now logged in as {user.username}")
            return redirect('index')

        else:
            pwd=user_form.password
            email=user_form.email
            if(messages in  user_form.as_data()):
                if messages == 'pwd':
                    messages.error(request,f"Selected password: {pwd} is not strong enough")
                if messages=='email':
                    messages.error(request,f"Declared {email} is not valid")
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
        if request.user.is_authenticated:
            return redirect('index')

        if request.method == 'POST':
            username = request.POST['username'].lower()
            password = request.POST['password']

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exist')
                return render(request, 'for1/users/user.login.html')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(request.GET['next'] if 'next' in request.GET else 'index')

            else:
                messages.error(request, 'Username OR password is incorrect')

    return render(request, 'for1/users/user.login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')