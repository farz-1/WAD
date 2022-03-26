from forms import UserForm, UserProfilePictureForm, UserProfileForm
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


class TestUserForm(TestCase):
    def testUsername(self):
        form = UserForm(data={'username': "Joe"})
        
        self.assertTrue(form.fields['username'].label is None
        or form.fields['username'].label == 'username')
        self.assertTrue(form.is_valid())

    def testEmail(self):
        form = UserForm(data={'email': "joelee90x@gmail.com"})
        self.assertTrue(form.fields['email'].label is None 
        or form.fields['email'].label == 'email')
        self.assertTrue(form.is_valid())

    def testPassword(self):
        form = UserForm('password': "F0xtr0t.41h4")
        
        self.assertTrue(form.fields['password'].label is None
        or form.fields['password'].label == 'password')
        self.assertTrue(form.is_valid())

class TestUserProfilePicureForm(TestCase):    
    def testProfilePicture(self):
        newPhoto.image = SimpleUploadedFile(name='test_image.jpg', content=open('../media/media/profile_images/car.png', 'rb').read(), content_type='image/jpeg')
        self.assertTrue(newPhoto.image)
        
        form = UserProfilePictureForm(data={'picture': newPhoto.image})
        self.assertTrue(form.is_valid())

class TestUserProfileForm(TestCase):
    def testFavCar(self):
        form = UserProfileForm(data={'favCar': ""})

        self.assertTrue(form.fields['favCar'].label is None
        or form.fields['favCar'].label == 'favCar')
        self.assertTrue(form.is_valid())


    def testFavTeam(self):
        form = UserForm(data={'favTeam': "Red Bull"})
        
        self.assertTrue(form.fields['favTeam'].label is None
        or form.fields['favTeam'].label == 'favTeam')
        self.assertTrue(form.is_valid())


    def testFavDriver(self):
        form = UserForm(data={'favDriver': "Max Verstappen"})
        
        self.assertTrue(form.fields['favCar'].label is None
        or form.fields['favDriver'].label == 'favDriver')
        self.assertTrue(form.is_valid())

    def testPicture(self):
        newPhoto.image = SimpleUploadedFile(name='test_image.jpg', content=open('../media/media/profile_images/car.png', 'rb').read(), content_type='image/jpeg')
        self.assertTrue(newPhoto.image)
        
        form = UserProfilePictureForm(data={'picture': newPhoto.image})
        self.assertTrue(form.is_valid())

class TestConstructorRatingForm(TestCase):
    def testOverallRating(self):
        form = ConstructorRatingForm(data={'overallRating': 3})
        
        self.assertTrue(form.fields['overallRating'].label is None
        or form.fields['overallRating'].label == 'overallRating')
        self.assertTrue(form.is_valid())
    
    def testTeamPrinciple(self):
        form = ConstructorRatingForm(data={'TeamPrinciple': 3})
        self.assertTrue(form.fields['teamPrinciple'].label is None
        or form.fields['teamPrinciple'].label == 'teamPrinciple')
        self.assertTrue(form.is_valid())


class TestDriverRatingForm(TestCase):
    def testOverallRating(self):
        form = DriverRatingForm(data={'overallRating': 3})

        self.assertTrue(form.fields['overallRating'].label is None
        or form.fields['overallRating'].label == 'overallRating')
        self.assertTrue(form.is_valid())

    def testRaceCraft(self):
        form = DriverRatingForm(data={'raceCraft': 3})

        self.assertTrue(form.fields['raceCraft'].label is None
        or form.fields['raceCraft'].label == 'raceCraft')
        self.assertTrue(form.is_valid())

class TestCarRatingForm(TestCase):
    def testOverallRating(self):
        form = CarRatingForm(data={'overallRating': 3})

        self.assertTrue(form.fields['overallRating'].label is None
        or form.fields['overallRating'].label == 'overallRating')
        self.assertTrue(form.is_valid())

    def testEngine(self):
        form = CarRatingForm(data={'engine': 3})

        self.assertTrue(form.fields['engine'].label is None
        or form.fields['engine'].label == 'engine')
        self.assertTrue(form.is_valid())

    

    



    
    
    



