from for1.forms import *
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


class TestUserForm(TestCase):
    def testUsername(self):
        form = UserForm(data={'username': "Joe",
        "email": "joelee90x@gmail.com",
        "password": "F0xtr0t.41h4"})
        self.assertTrue(form.is_valid())


"""
class TestUserProfilePicureForm(TestCase):    
    def testProfilePicture(self):
        newPhoto.image = SimpleUploadedFile(name='test_image.jpg', content=open('../media/profile_images/car.png', 'rb').read(), content_type='image/jpeg')
        self.assertTrue(newPhoto.image)
        
"""

"""
class TestUserProfileForm(TestCase):
    def testFavCar(self):
        data = {'favCar': "Red Bull Racing RB18",
        'favTeam': "Red Bull",
        'favDriver': "Max Verstappen",
        'aboutMe': "Some text"
        }

        file_data = {'picture': SimpleUploadedFile('../media/profile_images/default.jpg', 'data')}
        form = UserProfileForm(data, file_data)

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