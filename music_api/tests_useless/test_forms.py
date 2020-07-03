from django.test import TestCase
from music_api.forms import MelodyForm, CreateUserForm
from django.contrib.auth.models import User
from django.test import Client
from django.contrib.auth import authenticate

class TestModels(TestCase ):

    def test_user_form_correct_data(self):
        data = {
            'username': 'test',
            'email': 't@y.ru',
            'password1': 'testtest123',
            'password2': 'testtest123'}
        form = CreateUserForm(data)
        self.assertTrue(form.is_valid())

    def test_user_form_invalid_data(self):
        data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': ''}
        form = CreateUserForm(data)
        self.assertFalse(form.is_valid())


    def test_melody_form_correct_data(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        data = {
                   'user':'john',
                   'melody':'Unittest/test.wav',
                   'name':'test',
            'status':'Uploaded'}
        form = MelodyForm(data)
        self.assertFalse(form.is_valid())
        user.delete()

    def test_melody_form_invalid_data(self):
        data = {
                   'user':'',
                   'melody':'',
                   'name':'',
            'status':''}
        form = MelodyForm(data)
        self.assertFalse(form.is_valid())


    def test_form_user_field_label(self):
        form = MelodyForm()
        self.assertEquals(
            form.fields['user'].label, 'User')
