"""f1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from for1 import views_main, views_cars, views_drivers, views_constructors, views_profile, views_schedule, views_news, \
    views_leaderboard, views_users, views_home, views_login, views_register

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Views Main
    path('', views_main.index, name='index'),
    #path('about/', views_main.about, name='about'),
    path('register/', views_main.register, name='register'),
    path('login/', views_main.user_login, name='login'),

    # Views News
    path('news/', views_news.index, name='news'),

    # Views Leaderboard
    path('leaderboard/', views_leaderboard.index, name='leaderboard'),

    # Views Users
    # path('users/', views_users.index, name='users'),
    # path('user/<int:id>', views_users.details, name='user_details'),
    # path('user/<int:id>/edit', views_users.edit, name='user_edit'),

    # Views Schedule
    path('home/', views_home.index, name='home'),

    path('schedule/', views_schedule.index, name='schedule'),

    # Views Cars
    path('cars/', views_cars.index, name='cars'),
    path('login/', views_login.index, name='login'),
    path('register/', views_register.index, name='register'),

    # path('car/<int:id>', views_cars.details, name='car_details),
    path('car/<int:id>/rate', views_cars.rate, name='car_rate'),

    # Views Drivers
    path('profile/', views_profile.index, name='profile'),

    path('drivers/', views_drivers.index, name='drivers'),
    # path('driver/<int:id>', views_drivers.details, name='driver_details),
    # path('car/<int:id>/rate', views_drivers.rate, name='driver_rate'),

    # Views Constructors
    path('constructors/', views_constructors.index, name='constructors'),
    # path('constructor/<int:id>', views_constructors.details, name='constructor_details),
    # path('constructor/<int:id>/rate', views_constructors.rate, name='constructor_rate'),
]
