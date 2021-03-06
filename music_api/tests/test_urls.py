#import unittests
from django.test import TestCase
from django.urls import reverse, resolve
from music_api.views import MelodyView

class TestUrl(TestCase):

    def test_melodys_url_is_resolved(self):
        url = reverse('melodys')
        self.assertEquals(resolve(url).func.view_class,MelodyView)