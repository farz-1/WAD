from django.urls import path
from for1 import views_main

app_name = 'for1'
urlpatterns = [
    path('', views.index, name='index'),
]
