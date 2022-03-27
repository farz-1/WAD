from django.test import TestCase
from for1.models import *


class ConstructorTest(TestCase):   
    
    @classmethod
    def setupTestData(cls):
        Constructor.objects.create(name="Red Bull",
        teamPrincipal="Christian Horner",
        nationality="Austrian",
        yearsActive=17,
        raceEngineer="Gianpiero",
        about="Some mocked about text",
        slug ="red-bull",
        overallAverage = 5)
        print("YES YES YES YES YES YES")

    def testName(self):)
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    def testNameLength(self):
        constructor = Constructor.objects.get(name="Red Bull")
        max_length = constructor._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def testPrincipal(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('teamPrincipal').verbose_name
        self.assertEqual(field_label, 'TeamPrincipal')

    def testNationality(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('nationality').verbose_name
        self.assertEqual(field_label, 'Nationality')

    def testYearsActive(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('yearsActive').verbose_name
        self.assertEqual(field_label, 'YearsActive')

    def testRaceEngineer(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('raceEngineer').verbose_name
        self.assertEqual(field_label, 'RaceEngineer')

    def testAbout(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('about').verbose_name
        self.assertEqual(field_label, 'About')

    def testSlug(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'Slug')

    def testOverallAverage(self):
        constructor = Constructor.objects.get(name="Red Bull")
        field_label = constructor._meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'OverallAverage')

class DriverTest(TestCase):
    def setupDriver(cls):
        Driver.objects.create(name="Max Verstappen",
        DOB="30/09/1997",
        height="1.81m",
        weight="72kg",
        nationality="Belgian-Dutch",
        driverNumber="1",
        seasonsWon="1",
        podiumsWon="60",
        constructor="Red Bull",
        about="Mocked about text",
        slug="max-verstappen",
        overallAverage="3"
        )

    def testName(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    def testNameLength(self):
        driver = Driver.objects.get(name="Max Verstappen")
        max_length = driver._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def testDOB(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('DOB').verbose_name
        self.assertEqual(field_label, 'DOB')

    def testDOBLength(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('DOB').verbose_name
        self.assertEqual(len(field_label), 10)
    
    def testHeight(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('height').verbose_name
        self.assertEqual(field_label, 'Height')

    def testHeightLength(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('Height').verbose_name
        self.assertEqual(len(field_label), 5)

    def testWeight(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('weight').verbose_name
        self.assertEqual(field_label, 'Weight')

    def testWeightLength(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('height').verbose_name
        self.assertEqual(len(field_label), 5)

    def testNationality(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('nationality').verbose_name
        self.assertEqual(field_label, 'Nationality')

    def testDriverNumber(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('driverNumber').verbose_name
        self.assertEqual(field_label, 'DriverNumber')

    def testSeasonsWon(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('seasonsWon').verbose_name
        self.assertEqual(field_label, 'SeasonsWon')

    def testPodiumsWon(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('podiumsWon').verbose_name
        self.assertEqual(field_label, 'PodiumsWon')

    def testConstructor(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('constructor').verbose_name
        self.assertEqual(field_label, 'Constructor')

    def testAbout(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('about').verbose_name
        self.assertEqual(field_label, 'About')

    def testSlug(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'Slug')

    def testOverallAverage(self):
        driver = Driver.objects.get(name="Max Verstappen")
        field_label = driver._meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'OverallAverage')

# Testing all fields isn't really necessary, so I've decided to omit some
class TestCar(TestCase):
    def setupCar(cls):
        Car.objects.create(model="Red Bull Racing RB18",
        horsepower="740bhp",
        engine="HRC 90º V6",
        weight="1,753lbs",
        gearbox="Paddle Operated 8 speed Automatic",
        constructor="Red Bull",
        about="The Red Bull Racing RB18 is a Formula One car designed and constructed by Red Bull Racing to compete in the 2022 Formula One World Championship. It features Oracle as a new title sponsor, whose branding is visible on the engine cover. The RB18 will be driven by reigning Formula One World Champion Max Verstappen and Sergio Pérez. The chassis is Red Bull's first Formula One car under the 2022 technical regulations",
        slug="red-bull",
        overallAverage="0.00")

    def testModel(self):
        car = Car.objects.get(model="Red Bull Racing RB18")
        field_label = car._meta.get_field('model').verbose_name
        self.assertEqual(field_label, 'Model')
    
    def testHorsepower(self):
        car = Car.objects.get(model="Red Bull Racing RB18")
        field_label = car._meta.get_field('horsepower').verbose_name
        self.assertEqual(field_label, 'Horsepower')

    def testEngine(self):
        car = Car.objects.get(model="Red Bull Racing RB18")
        field_label = car._meta.get_field('engine').verbose_name
        self.assertEqual(field_label, 'Engine')

    def testGearbox(self):
        car = Car.objects.get(model="Red Bull Racing RB18")
        field_label = car._meta.get_field('gearbox').verbose_name
        self.assertEqual(field_label, 'Gearbox')

    def testConstructor(self):
        car = Car.objects.get(model="Red Bull Racing RB18")
        field_label = car._meta.get_field('constructor').verbose_name
        self.assertEqual(field_label, 'Constructor')

    def testOverallAverage(self):
        car = Car.objects.get(model="Red Bull Racing RB18")
        field_label = car._meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'OverallAverage')

class TestRace(TestCase):
    def setupRace(cls):
        Race.objects.create(location="Japan - Suzuka",
        trackLength="5.807km",
        date="07/10-09/10",
        laps="53",
        time="06:00-08:00")

    def testLocation(self):
        race = Race.objects.get(location="Japan- Suzuka")
        field_label = race.meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'Location')

    def testTrackLength(self):
        race = Race.objects.get(location="Japan- Suzuka")
        field_label = race.meta.get_field('trackLength').verbose_name
        self.assertEqual(field_label, 'TrackLength')

    def testLaps(self):
        race = Race.objects.get(location="Japan- Suzuka")
        field_label = race.meta.get_field('laps').verbose_name
        self.assertEqual(field_label, 'Laps')

    def testTime(self):
        race = Race.objects.get(location="Japan- Suzuka")
        field_label = race.meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'Time')

class TestNews(TestCase):
    def setupNews(cls):
        News.objects.create(title="Mock",
        summary="mocked even more",
        imageURL="https://s.yimg.com/ny/api/res/1.2/q7uYBoEQoNjIaHud6XY0lA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://s.yimg.com/uu/api/res/1.2/X49ns46fkyRfI9AJC3S64w--~B/aD01NzYwO3c9ODY0MDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/f9a4e6f4e827a07a26d41e724789bd74",
        articleURL="https://news.yahoo.com/fia-concludes-masi-made-human-145731017.html",
        published="2022-03-19 14:57:31",
        author="joe lee")

    def testTitle(self):
        news = News.objects.get(name="Mock")
        field_label = race.meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')

    def testImageURL(self):
        f = URLField()
        field_label = race.meta.get_field('imageURL').verbose_name
        self.assertEqual(field_label, 'ImageURL')

    def testArticleURL(self):
        news = News.objects.get(name="Mock")
        field_label = race.meta.get_field('articleURL').verbose_name
        self.assertEqual(field_label, 'ArticleURL')

    def testPublished(self):
        news = News.objects.get(name="Mock")
        field_label = race.meta.get_field('published').verbose_name
        self.assertEqual(field_label, 'Published')

class TestUserProfile(TestCase):
    def setupUserProfile(cls):
        UserProfile.objects.create(user="joe",
        favCar="Red Bull Racing RB18",
        favTeam="Red Bull",
        favDriver="Max Verstappen",
        aboutMe="mock",
        picture="",
        slug="joe")

    def testUser(self):
        userProfile = get_user_model().objects.last().profile

    def testFavCar(self):
        userProfile = UserProfile.objects.get(user="Joe")
        field_label = userProfile.meta.get_field('favCar').verbose_name
        self.assertEqual(field_label, 'FavCar')

    def testFavTeam(self):
        userProfile = UserProfile.objects.get(user="Joe")
        field_label = userProfile.meta.get_field('favTeam').verbose_name
        self.assertEqual(field_label, 'FavTeam')

    def testFavCar(self):
        userProfile = UserProfile.objects.get(user="Joe")
        field_label = userProfile.meta.get_field('favCar').verbose_name
        self.assertEqual(field_label, 'FavCar')

    def testFavDriver(self):
        userProfile = UserProfile.objects.get(user="Joe")
        field_label = userProfile.meta.get_field('favDriver').verbose_name
        self.assertEqual(field_label, 'FavDriver')

    def testFavDriver(self):
        userProfile = UserProfile.objects.get(user="Joe")
        field_label = userProfile.meta.get_field('favDriver').verbose_name
        self.assertEqual(field_label, 'FavDriver')

class TestDriverRating(TestCase):
    def setupDriverRating(cls):
        DriverRating.objects.create(driverID="Max Verstappen",
        userID="joe",
        lastModified="2022-03-27 00:09:32.276558",
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
        driverRating = DriverRating.objects.get(driverID="Max Verstappen")
        field_label = driverRating.meta.get_field('driverID').verbose_name
        self.assertEqual(field_label, 'DriverID')

    def testUserID(self):
        driverRating = DriverRating.objects.get(driverID="Max Verstappen")
        field_label = driverRating.meta.get_field('userID').verbose_name
        self.assertEqual(field_label, 'UserID')

    def testLastModified(self):
        driverRating = DriverRating.objects.get(driverID="Max Verstappen")
        field_label = driverRating.meta.get_field('lastModified').verbose_name
        self.assertEqual(field_label, 'LastModified')

    def testOverallAverage(self):
        driverRating = DriverRating.objects.get(driverID="Max Verstappen")
        field_label = driverRating.meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'OverallAverage')

    def testOverallRating(self):
        driverRating = DriverRating.objects.get(driverID="Max Verstappen")
        field_label = driverRating.meta.get_field('testOverallRating').verbose_name
        self.assertEqual(field_label, 'TestOverallRating')

    def testPersonality(self):
        driverRating = DriverRating.objects.get(driverID="Max Verstappen")
        field_label = driverRating.meta.get_field('personality').verbose_name
        self.assertEqual(field_label, 'Personality')

class TestConstructorRating(TestCase):
    def setupConstructorRating(cls):
        constructorRating = ConstructorRating.objects.create(constructorID="Red Bull",
        userID="joe",
        lastModified="2022-03-27 00:09:32.276558",
        overallAverage=3,
        overallRating=3,
        teamPrinciple=3,
        raceStrategy=3,
        pitStop=3)

    def testConstructorID(self):
        constructorRating = ConstructorRating.objects.get(constructorID="Red Bull")
        field_label = constructorRating.meta.get_field('constructorID').verbose_name
        self.assertEqual(field_label, 'ConstructorID')

    def testUserID(self):
        constructorRating = ConstructorRating.objects.get(constructorID="Red Bull")
        field_label = constructorRating.meta.get_field('userID').verbose_name
        self.assertEqual(field_label, 'UserID')

    def testLastModified(self):
        constructorRating = ConstructorRating.objects.get(constructorID="Red Bull")
        field_label = constructorRating.meta.get_field('lastModified').verbose_name
        self.assertEqual(field_label, 'LastModified')

    def testOverallAverage(self):
        constructorRating = ConstructorRating.objects.get(constructorID="Red Bull")
        field_label = constructorRating.meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'OverallAverage')

    def testTeamPrinciple(self):
        constructorRating = ConstructorRating.objects.get(constructorID="Red Bull")
        field_label = constructorRating.meta.get_field('teamPrinciple').verbose_name
        self.assertEqual(field_label, 'TeamPrinciple')

class TestCarRating(TestCase):
    def setupCarRating(cls):
        carRating = CarRating.objects.create(carID="Red Bull Racing RB18",
        userID="joe",
        lastModified="2022-03-27 00:09:32.276558",
        overallAverage=3,
        overallRating=3,
        speed=3,
        aerodynamics=3,
        aesthetics=3,
        braking=3,
        engine=3)

    def testCarID(self):
        carRating = CarRating.objects.get(carID="Red Bull Racing RB18")
        field_label = carRating.meta.get_field('carID').verbose_name
        self.assertEqual(field_label, 'CarID')

    def testUserID(self):
        carRating = CarRating.objects.get(carID="Red Bull Racing RB18")
        field_label = carRating.meta.get_field('userID').verbose_name
        self.assertEqual(field_label, 'UserID')

    def lastModified(self):
        carRating = CarRating.objects.get(carID="Red Bull Racing RB18")
        field_label = carRating.meta.get_field('lastModified').verbose_name
        self.assertEqual(field_label, 'LastModified')

    def testOverallAverage(self):
        carRating = CarRating.objects.get(carID="Red Bull Racing RB18")
        field_label = carRating.meta.get_field('overallAverage').verbose_name
        self.assertEqual(field_label, 'OverallAverage')

    def testBraking(self):
        carRating = CarRating.objects.get(carID="Red Bull Racing RB18")
        field_label = carRating.meta.get_field('braking').verbose_name
        self.assertEqual(field_label, 'Braking')


    

    


        
        

        

        
        
