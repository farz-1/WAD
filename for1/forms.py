from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from for1.models import UserProfile, DriverRating, CarRating, ConstructorRating


# driver ID/car ID/constructor ID and userID ?
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('favCar', 'favTeam', 'favDriver', 'aboutMe', 'picture',)


class ConstructorRatingForm(forms.ModelForm):
    overallAverage = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for overall average.")
    teamPrinciple = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for the team principle.")
    raceStrategy = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for the race strategy.")
    pitStop = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for the pit stop.")

    class Meta:
        model = ConstructorRating
        fields = ('overallAverage', 'teamPrinciple', 'raceStrategy', 'pitStop')


class DriverRatingForm(forms.ModelForm):
    overallAverage = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for overall average.")
    personality = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for personality.")
    aggressiveness = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for aggressiveness.")
    awareness = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for awareness.")
    experience = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for experience.")
    starts = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for starts.")
    pace = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for pace.")
    racecraft = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for racecraft.")

    class Meta:
        model = DriverRating
        fields = ('overallAverage', 'personality', 'aggressiveness', 'awareness', 'experience', 'starts', 'pace',
                  'racecraft')


class CarRatingForm(forms.ModelForm):
    overallAverage = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for overall average.")
    speed = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for speed.")
    aerodynamics = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for aerodynamics.")
    braking = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for braking.")
    engine = forms.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)],
            help_text="Please enter the rating between 1-5 for engine.")

    class Meta:
        model = CarRating
        fields = ('overallAverage', 'speed', 'aerodynamics', 'aesthetics', 'braking', 'engine')
