from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DriverRating(models.Model):
    driverID =
    
    userID = 
    
    created = models.DateTimeField(editable=False)
    
    lastModified = modified = models.DateTimeField()
    
    #overall average + all 
    overallAverage = 
    
    overallRating = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    
    personality = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    aggressiveness = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    awareness = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    experience = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    starts = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    pace = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    racecraft = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
    
    
class ConstructorRating(models.Model):

class CarRating(models.Model):

class Driver(models.Model):

class Constructor(models.Model):
    
class Car(models.Model):
    
class Races(models.Model):
    
class User(models.Model):