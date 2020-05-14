import random

from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, APILiveServerTestCase


class UserTest(APITestCase):

    def setUp(self):
        self.client.login(username='admin', password='123')
        self.client.login(username='john', password='johnpassword')

    def test_get_userList(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

    def test_get_user(self):
        url = reverse('user-detail', args=[1])
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {'username': 'ggy', 'password': '123'}
        url = reverse('user-list')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)

