from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "Test User",
            email = "test@pharmacy.com",
            password = "password"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "Test User")
        self.assertEqual(self.user.email, "test@pharmacy.com")
        self.assertTrue(self.user.check_password("password"))