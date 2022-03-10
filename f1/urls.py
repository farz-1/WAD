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

from for1 import views_main, views_cars

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Views Main
    path('', views_main.index, name='index'),
    #path('about/', views_main.about, name='about'),
    path('register/', views_main.register, name='register'),
    path('login/', views_main.user_login, name='login'),

    # Views Car
    path('cars/', views_cars.index, name='cars'),
    path('cars/ratings', views_cars.ratings, name='cars_ratings'),
]
