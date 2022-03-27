from django.test import TestCase
from django.urls import reverse

from for1.views_main import *

class TestDriverView(TestCase):
    def testUrl(self):
        response = self.client.get('/drivers/')
        self.assertEqual(response.status_code, 200)

    def testTemplate(self):
        response = self.client.get('/drivers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'for1/drivers/drivers.html')