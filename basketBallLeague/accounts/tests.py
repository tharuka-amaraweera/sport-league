from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="adminuser",
            password="admin1234"
        )

    def test_login(self):
        data = {
            "username": "adminuser",
            "password": "admin1234"
        }

        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get_or_create(user=self.user)
        alist = list(self.token)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+str(alist[0]))
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
