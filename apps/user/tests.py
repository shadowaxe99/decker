
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_user_has_auth_token(self):
        self.assertIsNotNone(self.user.auth_token)
