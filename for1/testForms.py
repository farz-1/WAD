from for1.forms import *
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


class TestUserForm(TestCase):
    def testUsername(self):
        form = UserForm(data={'username': "Joe",
        "email": "joelee90x@gmail.com",
        "password": "F0xtr0t.41h4"})
        self.assertTrue(form.is_valid())
<<<<<<< HEAD
=======

    def testPassword(self):
        form = UserForm('password': "F0xtr0t.41h4")
        
        self.assertTrue(form.fields['password'].label is None
        or form.fields['password'].label == 'password')
        self.assertTrue(form.is_valid())

class TestUserProfilePicureForm(TestCase):    
    def testProfilePicture(self):
        newPhoto.image = SimpleUploadedFile(name='test_image.jpg', content=open('../media/profile_images/car.png', 'rb').read(), content_type='image/jpeg')
        self.assertTrue(newPhoto.image)
>>>>>>> 5ae6cf206cdb6d2520ef57908bab900df0157d43
        
"""
class TestUserProfileForm(TestCase):
    def testFavCar(self):
        form = UserProfileForm(data={'favCar': "Red Bull Racing RB18",
        'favTeam': "Red Bull",
        'favDriver': "Max Verstappen",

        })

        self.assertTrue(form.fields['favCar'].label is None
        or form.fields['favCar'].label == 'favCar')
        self.assertTrue(form.is_valid())


    def testFavTeam(self):
        form = UserForm(data={'favTeam': "Red Bull"})
        
        self.assertTrue(form.fields['favTeam'].label is None
        or form.fields['favTeam'].label == 'favTeam')
        self.assertTrue(form.is_valid())


    def testFavDriver(self):
        form = UserForm(data={})
        
        self.assertTrue(form.fields['favCar'].label is None
        or form.fields['favDriver'].label == 'favDriver')
        self.assertTrue(form.is_valid())

    def testPicture(self):
        newPhoto.image = SimpleUploadedFile(name='test_image.jpg', content=open('../media/profile_images/car.png', 'rb').read(), content_type='image/jpeg')
        self.assertTrue(newPhoto.image)
        
        form = UserProfilePictureForm(data={'picture': newPhoto.image})
        self.assertTrue(form.is_valid())
"""

class TestConstructorRatingForm(TestCase):
    def testOverallRating(self):
        form = ConstructorRatingForm(data={'overallRating': 3,
        'teamPrinciple': 3,
        'raceStrategy': 3,
        'pitStop': 3
        })
        
        self.assertTrue(form.is_valid())
    

class TestDriverRatingForm(TestCase):
    def testOverallRating(self):
        form = DriverRatingForm(data={'overallRating': 3,
        'personality':3,
        'aggressiveness':3,
        'awareness':3,
        'experience':3,
        'starts':3,
        'pace':3,
        'racecraft':3})

        self.assertTrue(form.is_valid())

class TestCarRatingForm(TestCase):
    def testOverallRating(self):
        form = CarRatingForm(data={'overallRating': 3,
        'speed':3,
        'aerodynamics':3,
        'aesthetics':3,
        'braking':3,
        'engine':3})

        self.assertTrue(form.is_valid())