from rest_framework.test import APITestCase

from .models import User


class IsAuthenticatedAndCanWriteUserOrReadOnlyTestCase(APITestCase):
    """
    Test the IsAuthenticatedAndCanWriteUserOrReadOnly class
    """

    def setUp(self):
        User.objects.create_user(id=1, username='u1')
        User.objects.create_user(id=2, username='u2', is_staff=True)

    def test_no_user(self):
        self.assertEqual(self.client.get('/accounts/1/').status_code, 403)
        self.assertEqual(self.client.patch('/accounts/1/').status_code, 403)

    def test_regular_user(self):
        self.client.force_authenticate(User.objects.get(pk=1))
        self.assertEqual(self.client.get('/accounts/1/').status_code, 200)
        self.assertEqual(self.client.patch('/accounts/1/').status_code, 200)
        self.assertEqual(self.client.patch('/accounts/2/').status_code, 403)

    def test_admin_user(self):
        self.client.force_authenticate(User.objects.get(pk=2))
        self.assertEqual(self.client.patch('/accounts/1/').status_code, 200)
