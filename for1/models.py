from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.utils import timezone
from django.template.defaultfilters import slugify
from decimal import *


class Constructor(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    teamPrincipal = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    yearsActive = models.IntegerField()
    raceEngineer = models.CharField(max_length=50)
    about = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    overallAverage = models.DecimalField(max_digits=4, decimal_places=2,null=True,default=0.0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Constructor, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Constructors'

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    DOB = models.CharField(max_length=10)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    nationality = models.CharField(max_length=20)
    driverNumber = models.IntegerField()
    seasonsWon = models.IntegerField()
    podiumsWon = models.IntegerField()
    constructor = models.ForeignKey(Constructor, on_delete=models.SET_NULL,null=True)
    about = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    overallAverage = models.DecimalField(max_digits=4, decimal_places=2,null=True,default=0.0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Driver, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=50, primary_key=True)
    horsepower = models.CharField(max_length=5)
    engine = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    gearbox = models.CharField(max_length=50)
    constructor = models.ForeignKey(Constructor, on_delete=models.SET_NULL, null=True)
    about = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    overallAverage = models.DecimalField(max_digits=4, decimal_places=2,null=True,default=0.0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.constructor.name)
        super(Car, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.model


class Race(models.Model):
    location = models.CharField(max_length=20, primary_key=True)
    trackLength = models.CharField(max_length=5)
    date = models.CharField(max_length=10)
    laps = models.IntegerField()
    time = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.location


class News(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=256)
    imageURL = models.URLField(null=True)
    articleURL = models.URLField()
    published = models.DateTimeField()
    author = models.CharField(max_length=30, null=True)
    
    class Meta:
        verbose_name_plural='News'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favCar = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    favTeam = models.ForeignKey(Constructor, on_delete=models.SET_NULL, null=True)
    favDriver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    aboutMe = models.CharField(max_length=256,null=True)
    picture = models.ImageField(upload_to='media/profile_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class DriverRating(models.Model):
    driverID = models.ForeignKey(Driver, on_delete=models.CASCADE)

    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    lastModified = models.DateTimeField(null=True)

    overallAverage = models.DecimalField(max_digits=4, decimal_places=2,null=True)

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

    class Meta:
        verbose_name_plural = 'DriverRatings'

    @property
    def get_overall_average(self):
        scores = [self.overallRating, self.personality, self.aggressiveness, self.awareness, self.experience,
                  self.starts, self.pace, self.racecraft]  # add new fields here.
        return sum(scores) / len(scores)  # this way allows for easier adding of new fields in future.
    
    @property
    def get_total_overall_average(self):
        total=self.overallAverage
        rating_count=1
        driver_rating_set = DriverRating.objects.filter(driverID=self.driverID)

    
        driver = Driver.objects.get(name=self.driverID.name)
        for rating in driver_rating_set.iterator():
                total=total+float(rating.overallAverage)
                rating_count+=1
                
        return total/rating_count

    def save(self, *args, **kwargs):
        self.overallAverage = self.get_overall_average
        ''' On save, update timestamps '''
        self.lastModified = timezone.now()
        update = Driver.objects.get(name=self.driverID.name)
        driver_rating_set = DriverRating.objects.filter(driverID=self.driverID)
        if len(driver_rating_set)!=0:
            new_rating = self.get_total_overall_average
            update.overallAverage=new_rating
        else:
            update.overallAverage=self.overallAverage
        update.save()
        return super(DriverRating, self).save(*args, **kwargs)


class ConstructorRating(models.Model):
    constructorID = models.ForeignKey(Constructor, on_delete=models.CASCADE)

    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    lastModified = models.DateTimeField(null=True)

    overallAverage = models.DecimalField(max_digits=4, decimal_places=2,null=True)

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

    class Meta:
        verbose_name_plural = 'ConstructorRatings'

    @property
    def get_overall_average(self):
        scores = [self.overallRating, self.teamPrinciple, self.raceStrategy, self.pitStop]  # add new fields here.
        return sum(scores) / len(scores)  # this way allows for easier adding of new fields in future.

    @property
    def get_total_overall_average(self):
        total=self.overallAverage
        rating_count=1
        constructor_rating_set = ConstructorRating.objects.filter(constructorID=self.constructorID)

    
        constructor = Constructor.objects.get(name=self.constructorID.name)
        for rating in constructor_rating_set.iterator():
                total=total+float(rating.overallAverage)
                rating_count+=1
                
        return total/rating_count

    def save(self, *args, **kwargs):
        self.overallAverage = self.get_overall_average
        ''' On save, update timestamps '''
        self.lastModified = timezone.now()
        update = Constructor.objects.get(name=self.constructorID.name)
        constructor_rating_set = ConstructorRating.objects.filter(constructorID=self.constructorID)
        if len(constructor_rating_set)!=0:
            new_rating = self.get_total_overall_average
            update.overallAverage=new_rating
        else:
            update.overallAverage=self.overallAverage
        update.save()
        return super(ConstructorRating, self).save(*args, **kwargs)

class CarRating(models.Model):
    carID = models.ForeignKey(Car, on_delete=models.CASCADE)

    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    lastModified = models.DateTimeField(null=True)

    overallAverage = models.DecimalField(max_digits=4, decimal_places=2,null=True)

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

    aesthetics = models.IntegerField(
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

    class Meta:
        verbose_name_plural = 'CarRatings'

    @property
    def get_overall_average(self):
        scores = [self.overallRating, self.speed, self.aerodynamics, self.aesthetics, self.braking,
                  self.engine]  # add new fields here.
        return sum(scores) / len(scores)  # this way allows for easier adding of new fields in future.
    
    @property
    def get_total_overall_average(self):
        total=self.overallAverage
        rating_count=1
        car_rating_set = CarRating.objects.filter(carID=self.carID)

    
        car = Car.objects.get(constructor=self.carID.constructor)
        for rating in car_rating_set.iterator():
                total=total+float(rating.overallAverage)
                rating_count+=1
                
        return total/rating_count

    def save(self, *args, **kwargs):
        self.overallAverage = self.get_overall_average
        ''' On save, update timestamps '''
        self.lastModified = timezone.now()
        update = Car.objects.get(constructor=self.carID.constructor)
        car_rating_set = CarRating.objects.filter(carID=self.carID)
        if len(car_rating_set)!=0:
            new_rating = self.get_total_overall_average
            update.overallAverage=new_rating
        else:
            update.overallAverage=self.overallAverage
        update.save()
        return super(CarRating, self).save(*args, **kwargs)
    
    
