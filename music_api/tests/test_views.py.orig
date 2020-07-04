from django.test import TestCase, Client
from django.urls import reverse
from music_api.forms import CreateUserForm, MelodyForm
from music_api.models import Melody
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

import json



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.userdata = {
            'username': 'test',
            'email': 't@y.ru',
            'password1': 'testtest123',
            'password2': 'testtest123'
        }
        self.log_pass = {
            'username': 'john',
            'password': 'johnpassword'
        }
        self.melodydata = {'user':'john',
                           'melody':'testmelody',
                           'name':'test_files/test.wav',
                           'status':'Uploaded'
        }
        self.home_url = reverse('home')
        self.reg = reverse('register')
        self.login = reverse('login')
        self.profile = reverse('profile')
        self.upload = reverse('upload')

    def login_user(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        #return user

    def test_home_is_authenticated(self):
        self.login_user()
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_not_authenticated(self):

        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 302)

    def test_registerPage_GET(self):

        response = self.client.get(self.reg)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_registerPage_POST(self):

        response = self.client.post(self.reg,self.userdata)
        self.assertEquals(response.status_code, 302)
        user = User.objects.values().first()
        self.assertEquals(user.get('username'), 'test' )

    def test_registerPage_is_authenticated(self):

        self.login_user()
        response = self.client.get(self.reg)
        self.assertEquals(response.status_code, 302)



    def test_loginPage_is_authenticated(self):

        self.login_user()
        response = self.client.get(self.login)
        self.assertEquals(response.status_code, 302)

    def test_loginPage_GET(self):

        response = self.client.get(self.login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_loginPage_validuser_POST(self):

        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        response = self.client.post(self.login, self.log_pass)
        self.assertEquals(response.status_code, 302)
        user = User.objects.values().first()
        self.assertEquals(user.get('username'), 'john')

    def test_loginPage_invaliduser_POST(self):
        incorrect_log_pass = {
            'username': 'kiki',
            'password': 'qwerty'
        }
        response = self.client.post(self.login, incorrect_log_pass)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Username OR password is incorrect')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_profilePage(self):
        self.login_user()
        response = self.client.get(self.profile)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/profile.html')

    def test_upload_GET(self):
        self.login_user()
        response = self.client.get(self.upload)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')

    '''
    def test_upload_POST(self):
        self.login_user()
        response = self.client.post(self.upload, self.melodydata)
        #print(Melody.objects.latest('name'))


        #self.assertEquals(response.status_code, 302)

    '''