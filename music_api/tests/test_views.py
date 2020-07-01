from django.test import TestCase, Client
from django.urls import reverse
from music_api.forms import CreateUserForm
from music_api.models import Melody
from django.contrib.auth.models import User
import json



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {
            'username': 'test',
            'email': 't@y.ru',
            'password1': 'testtest123',
            'password2': 'testtest123'
        }

        self.home_url = reverse('home')
        self.reg = reverse('register')

    '''
    def test_home(self):
        response = self.client.get(self.home_url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    '''
    def test_registerPage_GET(self):

        response = self.client.get(self.reg)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_registerPage_POST(self):

        response = self.client.post(self.reg,self.data)
        self.assertEquals(response.status_code, 302)
        user = User.objects.values().first()
        self.assertEquals(user.get('username'), 'test' )

    def test_registerPage_is_authenticated(self):

        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        response = self.client.get(self.reg)
        self.assertEquals(response.status_code, 302)
