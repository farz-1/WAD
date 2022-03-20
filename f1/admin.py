from django.contrib import admin
from f1.models import Constructor, Driver, Car, Race, News, User, DriverRating, ConstructorRating, CarRating

# Register your models here.
admin.site.register(Constructor)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Race)
admin.site.register(News)
admin.site.register(User)
admin.site.register(DriverRating)
admin.site.register(ConstructorRating)
admin.site.register(CarRating)