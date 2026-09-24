from django.contrib.auth import get_user_model
from django.test import Client, TestCase


User = get_user_model()

class AuthApiTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        