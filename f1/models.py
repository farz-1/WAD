from django.core.validators import MaxValueValidator, MinValueValidator
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
    
    overallRating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    
    personality = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    aggressiveness = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    awareness = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    experience = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    starts = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    pace = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    racecraft = models.IntegerField(
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
    constructorID =

    userID =

    created = models.DateTimeField(editable=False)

    lastModified = modified = models.DateTimeField()

    overallAverage =

    overallRating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    teamPrinciple = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    raceStrategy = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    pitStop = models.IntegerField(
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

class CarRating(models.Model):
    carID =

    userID =

    created = models.DateTimeField(editable=False)

    lastModified = modified = models.DateTimeField()

    overallAverage =

    overallRating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    speed = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    aerodynamics = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    Aesthetics = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    braking = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    engine = models.IntegerField(
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

class Driver(models.Model):
    name = models.CharField(max_length=50)
    DOB = models.DateField()
    picture = models.ImageField()
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    nationality = models.CharField(max_length=20)
    driverNumber = models.CharField(max_length=2)
    seasonsWon = models.IntegerField(max_length=5)

class Constructor(models.Model):
    name = models.CharField(max_length=50)
    teamPrincipal = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    yearsActive = models.IntegerField(max_length=2)
    raceEngineer = models.CharField(max_length=50)
    
class Car(models.Model):
    model = models.CharField(max_length=30)
    horsepower = models.CharField(max_length=5)
    engineSupplier = models.CharField(max_length=30)
    picture = models.ImageField()
    gearbox = models.CharField(max_length=30)
    
class Races(models.Model):
    location = models.CharField(max_length=20)
    trackLength = models.CharField(max_length=5)
    date = models.DateField()
    laps = models.CharField(max_length=5)
    raceWeekend = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    duration = models.FloatField()

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    userID = models.CharField(max_length=30)
    picture = models.ImageField()
    favCar = models.CharField(max_length=50)
    favTeam = models.CharField(max_length=50)
    favDriver = models.CharField(max_length=50)
    aboutMe = models.CharField(max_length=256)