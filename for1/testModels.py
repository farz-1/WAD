from django.test import TestCase
from models import Constructor
from models import Driver

class ConstructorTest(TestCase):
    def setUpConstructor(cls):
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

        

    




