from django.test import TestCase
from django.urls import reverse

from for1.views_main import *

class TestCarView(TestCase):
    def testUrl(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 200)

    def testTemplate(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'for1/cars/cars.html')