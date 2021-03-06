import os

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Melody


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MelodyForm(ModelForm):
    class Meta:
        model = Melody
        fields = ['user', 'melody', 'name', 'status']

    def is_ok(self, mel):
        ext = str(mel).split('.')[-1]
        if ext.lower() == 'wav':
            return True
        else:
            return False

