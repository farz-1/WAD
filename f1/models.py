from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Constructor(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    teamPrincipal = models.CharField(max_length=50, null=False)
    nationality = models.CharField(max_length=20, null=False)
    yearsActive = models.IntegerField(null=False)
    raceEngineer = models.CharField(max_length=50, null=False)
    

    class Meta:
        verbose_name_plural = 'Constructors'

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    DOB = models.CharField(max_length=10, null=False)
    picture = models.ImageField(null=False)
    height = models.CharField(max_length=5, null=False)
    weight = models.CharField(max_length=5, null=False)
    nationality = models.CharField(max_length=20, null=False)
    driverNumber = models.IntegerField(null=False)
    seasonsWon = models.IntegerField(null=False)
    podiumsWon = models.IntegerField(null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=30, null=False, unique=True)
    horsepower = models.CharField(max_length=5, null=False)
    engineSupplier = models.CharField(max_length=30, null=False)
    picture = models.ImageField(null=False)
    gearbox = models.CharField(max_length=30, null=False)
    constructor = models.ForeignKey(Constructor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.model


class Race(models.Model):
    location = models.CharField(max_length=20, null=False, unique=True)
    trackLength = models.CharField(max_length=5, null=False)
    date = models.CharField(max_length=10, null=False)
    laps = models.IntegerField(null=False)
    time = models.CharField(max_length=20, null=False)

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


class User(models.Model):
    username = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=30, null=False)
    userID = models.CharField(max_length=30, null=False, unique=True)
    picture = models.ImageField()
    favCar = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    favTeam = models.ForeignKey(Constructor, on_delete=models.SET_NULL, null=True)
    favDriver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    aboutMe = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.userID + " " + self.name


class DriverRating(models.Model):
    driverID = models.ForeignKey(Driver, on_delete=models.CASCADE, null=False)

    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    created = models.DateTimeField(editable=False, null=False)

    lastModified = models.DateTimeField(null=False)

    overallAverage = models.DecimalField(max_digits=4, decimal_places=2)

    overallRating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    personality = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )
    aggressiveness = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )
    awareness = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )
    experience = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )
    starts = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )
    pace = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )
    racecraft = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    class Meta:
        verbose_name_plural = 'DriverRatings'

    @property
    def get_overall_average(self):
        scores = [self.overallRating, self.personality, self.aggressiveness, self.awareness, self.experience,
                  self.starts, self.pace, self.racecraft]  # add new fields here.
        return sum(scores) / len(scores)  # this way allows for easier adding of new fields in future.

    def __str__(self):
        return self.userID + " " + self.driverID

    def save(self, *args, **kwargs):
        self.overallAverage = self.get_overall_average
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)


class ConstructorRating(models.Model):
    constructorID = models.ForeignKey(Constructor, on_delete=models.CASCADE, null=False)

    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    created = models.DateTimeField(editable=False, null=False)

    lastModified = models.DateTimeField(null=False)

    overallAverage = models.DecimalField(max_digits=4, decimal_places=2)

    overallRating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    teamPrinciple = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    raceStrategy = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    pitStop = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    class Meta:
        verbose_name_plural = 'ConstructorRatings'

    @property
    def get_overall_average(self):
        scores = [self.overallRating, self.teamPrinciple, self.raceStrategy, self.pitStop]  # add new fields here.
        return sum(scores) / len(scores)  # this way allows for easier adding of new fields in future.

    def __str__(self):
        return self.userID + " " + self.constructorID

    def save(self, *args, **kwargs):
        self.overallAverage = self.get_overall_average
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)


class CarRating(models.Model):
    carID = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)

    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    created = models.DateTimeField(editable=False, null=False)

    lastModified = models.DateTimeField(null=False)

    overallAverage = models.DecimalField(max_digits=4, decimal_places=2)

    overallRating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    speed = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    aerodynamics = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    aesthetics = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    braking = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    engine = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], null=False
    )

    class Meta:
        verbose_name_plural = 'CarRatings'

    @property
    def get_overall_average(self):
        scores = [self.overallRating, self.speed, self.aerodynamics, self.aesthetics, self.braking,
                  self.engine]  # add new fields here.
        return sum(scores) / len(scores)  # this way allows for easier adding of new fields in future.

    def __str__(self):
        return self.userID + " " + self.carID

    def save(self, *args, **kwargs):
        self.overallAverage = self.get_overall_average
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
