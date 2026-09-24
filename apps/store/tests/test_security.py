from django.contrib.auth.models import User
from django.test import TestCase

from core.security import create_jwt_token, decode_jwt_token

class TestCaseJWT(TestCase):
    def setUp(self):
        



        return super().setUp()