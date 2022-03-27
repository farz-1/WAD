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
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from for1 import views_main, views_cars, views_drivers, views_constructors, views_schedule, views_news, views_users

urlpatterns = [
    # Accounts
    path('accounts/login/', views_users.user_login, name='login'),
    path('accounts/logout/', views_users.logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # Views Main
    path('', views_main.index, name='index'),
    path('home/', views_main.home, name='home'),

    # Views News
    path('news/', views_news.index, name='news'),

    # Views Profile
    path('profile/', views_users.index, name='profile'),
    path('profile/edit/', views_users.edit, name='profile_edit'),
    path('register/', views_users.register, name='register'),
    path('login/', views_users.user_login, name='login'),

    # Views Schedule
    path('schedule/', views_schedule.index, name='schedule'),

    # Views Cars
    path('cars/', views_cars.index, name='cars'),
    path('cars/leaderboard', views_cars.leaderboard, name='cars_leaderboard'),
    path('car/<slug:slug>', views_cars.details, name='car_details'),
    path('car/<slug:slug>/rate', views_cars.rate, name='car_rate'),

    # Views Drivers
    path('drivers/', views_drivers.index, name='drivers'),
    path('drivers/leaderboard', views_drivers.leaderboard, name='drivers_leaderboard'),
    path('driver/<slug:slug>', views_drivers.details, name='driver_details'),
    path('driver/<slug:slug>/rate', views_drivers.rate, name='driver_rate'),

    # Views Constructors
    path('constructors/', views_constructors.index, name='constructors'),
    path('constructors/leaderboard', views_constructors.leaderboard, name='constructors_leaderboard'),
    path('constructor/<slug:slug>', views_constructors.details, name='constructor_details'),
    path('constructor/<slug:slug>/rate', views_constructors.rate, name='constructor_rate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)