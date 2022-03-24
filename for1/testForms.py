from forms import UserForm
from django.test import TestCase

class UserFormTest(TestCase):
    def testPassword() {
        form = UserForm()
        self.assertTrue(form.fields['password'].label is None
        or form.fields['password'].label == 'password')
    }