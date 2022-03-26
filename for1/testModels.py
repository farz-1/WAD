from django.test import TestCase
from models import *


class ConstructorTest(TestCase):
    def setupConstructor(cls):
        Constructor.objects.create(name="Mercedes", 
        teamPrincipal="Toto Wolff",
        nationality="Germany",
        yearsActive=68,
        raceEngineer="Peter Bonnington",
        about="Mercedes - everyone knows Mercedes.",
        slug ="Mercedes",
        overallAverage = 4.5)

    def testName(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def testNameLength(self):
        constructor = Constructor.objects.get(id=1)
        max_length = constructor._meta.get_field('name').max_length
        self.assertEqual(max_length, '50')

    def testPrincipal(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('teamPrincipal').verbose_name
        self.assertEqual(field_label, 'teamPrincipal')

    def testNationality(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('nationality').verbose_name
        self.assertEqual(field_label, 'nationality')

    def testYearsActive(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('yearsActive').verbose_name
        self.assertEqual(field_label, 'yearsActive')

    def testRaceEngineer(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('raceEngineer').verbose_name
        self.assertEqual(field_label, 'raceEngineer')

    def testAbout(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('about').verbose_name
        self.assertEqual(field_label, 'about')

    def testSlug(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def testOverallAverage(self):
        constructor = Constructor.objects.get(id=1)
        field_label = constructor._meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'overallAverage')

class DriverTest(TestCase):
    def setupDriver(cls):
        Driver.objects.create(name="Lewis Hamilton",
        DOB="",
        height="",
        weight="",
        nationality="Great Britain",
        driverNumber="",
        seasonsWon="",
        podiumsWon="",
        constructor="",
        about="Lewis Hamilton - some people love him; some people hate him",
        slug="",
        overallAverage=""
        )

    def testName(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def testNameLength(self):
        driver = Driver.objects.get(id=1)
        max_length = driver._meta.get_field('name').max_length
        self.assertEqual(max_length, '50')

    def testDOB(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('DOB').verbose_name
        self.assertEqual(field_label, 'DOB')

    def testDOBLength(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('DOB').verbose_name
        self.assertEqual(len(field_label), 10)
    
    def testHeight(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('height').verbose_name
        self.assertEqual(field_label, 'height')

    def testHeightLength(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('height').verbose_name
        self.assertEqual(len(field_label), 5)

    def testWeight(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('weight').verbose_name
        self.assertEqual(field_label, 'weight')

    def testWeightLength(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('height').verbose_name
        self.assertEqual(len(field_label), 5)

    def testNationality(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('nationality').verbose_name
        self.assertEqual(field_label, 'nationality')

    def testDriverNumber(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('driverNumber').verbose_name
        self.assertEqual(field_label, 'driverNumber')

    def testSeasonsWon(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('seasonsWon').verbose_name
        self.assertEqual(field_label, 'seasonsWon')

    def testPodiumsWon(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('podiumsWon').verbose_name
        self.assertEqual(field_label, 'podiumsWon')

    def testConstructor(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('constructor').verbose_name
        self.assertEqual(field_label, 'constructor')

    def testAbout(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('about').verbose_name
        self.assertEqual(field_label, 'about')

    def testSlug(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def testOverallAverage():
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'overallAverage')

# Testing all fields isn't really necessary, so I've decided to omit some
class TestCar(TestCase):
    def setupCar(cls):
        Car.objects.create(model="",
        horsepower="",
        engine="",
        weight="",
        gearbox="",
        constructor="",
        about="",
        slug="",
        overallAverage="")

    def testModel(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('model').verbose_name
        self.assertEqual(field_label, 'model')
    
    def testHorsepower(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('horsepower').verbose_name
        self.assertEqual(field_label, 'horsepower')

    def testEngine(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('engine').verbose_name
        self.assertEqual(field_label, 'engine')

    def testGearbox(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('gearbox').verbose_name
        self.assertEqual(field_label, 'gearbox')

    def testConstructor(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('constructor').verbose_name
        self.assertEqual(field_label, 'constructor')

    def testOverallAverage(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'overallAverage')

class TestRace(TestCase):
    def setupRace(cls):
        Race.objects.create(location="",
        trackLength="",
        date="",
        laps="",
        time="")

    def testLocation(self):
        race = Race.objects.get(id=1)
        field_label = race.meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'location')

    def testTrackLength(self):
        race = Race.objects.get(id=1)
        field_label = race.meta.get_field('trackLength').verbose_name
        self.assertEqual(field_label, 'trackLength')

    def testLaps(self):
        race = Race.objects.get(id=1)
        field_label = race.meta.get_field('laps').verbose_name
        self.assertEqual(field_label, 'laps')

    def testTime(self):
        race = Race.objects.get(id=1)
        field_label = race.meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'time')

class TestNews(TestCase):
    def setupNews(cls):
        News.objects.create(title="",
        summary="",
        imageURL="",
        articleURL="",
        published="",
        author="")

    def testTitle(self):
        news = News.objects.get(id=1)
        field_label = race.meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def testImageURL(self):
        f = URLField()
        field_label = race.meta.get_field('imageURL').verbose_name
        #self.assert

    def testArticleURL(self):
        news = News.objects.get(id=1)
        field_label = race.meta.get_field('articleURL').verbose_name
        self.assertEqual(field_label, 'articleURL')

    def testPublished(self):
        news = News.objects.get(id=1)
        field_label = race.meta.get_field('published').verbose_name
        self.assertEqual(field_label, 'published')

class TestUserProfile(TestCase):
    def setupUserProfile(cls):
        UserProfile.objects.create(user="",
        favCar="",
        favTeam="",
        favDriver="",
        aboutMe="",
        picture="",
        slug="")

    def testUser(self):
        userProfile = get_user_model().objects.last().profile

    def testFavCar(self):
        userProifle = UserProfile.objects.get(id=1)
        field_label = userProfile.meta.get_field('favCar').verbose_name
        self.assertEqual(field_label, 'favCar')

    def testFavTeam(self):
        userProifle = UserProfile.objects.get(id=1)
        field_label = userProfile.meta.get_field('favTeam').verbose_name
        self.assertEqual(field_label, 'favTeam')

    def testFavCar(self):
        userProifle = UserProfile.objects.get(id=1)
        field_label = userProfile.meta.get_field('favCar').verbose_name
        self.assertEqual(field_label, 'favCar')

    def testFavDriver(self):
        userProifle = UserProfile.objects.get(id=1)
        field_label = userProfile.meta.get_field('favDriver').verbose_name
        self.assertEqual(field_label, 'favDriver')

    def testFavDriver(self):
        userProifle = UserProfile.objects.get(id=1)
        field_label = userProfile.meta.get_field('favDriver').verbose_name
        self.assertEqual(field_label, 'favDriver')

class TestDriverRating(TestCase):
    def setupDriverRating(cls):
        DriverRating.objects.create(driverID="",
        userID="",
        lastModified="",
        overallAverage=3,
        overallRating=3,
        personality=3,
        aggressiveness=3,
        awareness=3,
        experience=3,
        starts=3,
        pace=3,
        racecraft=3)

    def testUserID(self):
        driverRating = DriverRating.objects.get(id=1)
        field_label = driverRating.meta.get_field('driverID').verbose_name
        self.assertEqual(field_label, 'driverID')

    def testUserID(self):
        driverRating = DriverRating.objects.get(id=1)
        field_label = driverRating.meta.get_field('userID').verbose_name
        self.assertEqual(field_label, 'userID')

    def testLastModified(self):
        driverRating = DriverRating.objects.get(id=1)
        field_label = driverRating.meta.get_field('lastModified').verbose_name
        self.assertEqual(field_label, 'lastModified')

    def testOverallAverage(self):
        driverRating = DriverRating.objects.get(id=1)
        field_label = driverRating.meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'overallAverage')

    def testOverallRating(self):
        driverRating = DriverRating.objects.get(id=1)
        field_label = driverRating.meta.get_field('testOverallRating').verbose_name
        self.assertEqual(field_label, 'testOverallRating')

    def testPersonality(self):
        driverRating = DriverRating.objects.get(id=1)
        field_label = driverRating.meta.get_field('personality').verbose_name
        self.assertEqual(field_label, 'personality')

class TestConstructorRating(TestCase):
    def setupConstructorRating(cls):
        constructorRating = ConstructorRating.objects.create(constructorID="",
        userID="",
        lastModified="",
        overallAverage=3,
        overallRating=3,
        teamPrinciple=3,
        raceStrategy=3,
        pitStop=3)

    def testConstructorID(self):
        constructorRating = ConstructorRating.objects.get(id=1)
        field_label = constructorRating.meta.get_field('constructorID').verbose_name
        self.assertEqual(field_label, 'constructorID')

    def testUserID(self):
        constructorRating = ConstructorRating.objects.get(id=1)
        field_label = constructorRating.meta.get_field('userID').verbose_name
        self.assertEqual(field_label, 'userID')

    def testLastModified(self):
        constructorRating = ConstructorRating.objects.get(id=1)
        field_label = constructorRating.meta.get_field('lastModified').verbose_name
        self.assertEqual(field_label, 'lastModified')

    def testOverallAverage(self):
        constructorRating = ConstructorRating.objects.get(id=1)
        field_label = constructorRating.meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'overallAverage')

    def testTeamPrinciple(self):
        constructorRating = ConstructorRating.objects.get(id=1)
        field_label = constructorRating.meta.get_field('teamPrinciple').verbose_name
        self.assertEqual(field_label, 'teamPrinciple')

class CarRating(TestCase):
    def setupCarRating(cls):
        carRating = CarRating.objects.create(carID="",
        userID="",
        lastModified="",
        overallAverage=3,
        overallRating=3,
        speed=3,
        aerodynamics=3,
        aesthetics=3,
        braking=3,
        engine=3)

    def testCarID(self):
        carRating = CarRating.objects.get(id=1)
        field_label = carRating.meta.get_field('carID').verbose_name
        self.assertEqual(field_label, 'carID')

    def testUserID(self):
        carRating = CarRating.objects.get(id=1)
        field_label = carRating.meta.get_field('userID').verbose_name
        self.assertEqual(field_label, 'userID')

    def lastModified(self):
        carRating = CarRating.objects.get(id=1)
        field_label = carRating.meta.get_field('lastModified').verbose_name
        self.assertEqual(field_label, 'lastModified')

    def testOverallAverage(self):
        carRating = CarRating.objects.get(id=1)
        field_label = carRating.meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'overallAverage')

    def testBraking(self):
        carRating = CarRating.objects.get(id=1)
        field_label = carRating.meta.get_field('braking').verbose_name
        self.assertEqual(field_label, 'braking')


    

    


        
        

        

        
        
