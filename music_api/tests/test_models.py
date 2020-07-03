from music_api.models import Melody
from django.test import TestCase
from django.contrib.auth.models import User
from pytest.ini import DJANGO_SETTINGS_MODULE

class TestModels(TestCase ):

    def setUP(self):
        self.melody1 = Melody.objects.crete(
            name = 'Melody 1'
        )

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        #example_object = models.ExampleModel({'file': "foo.bar"})
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Melody.objects.create(
            user = user,
            melody = 'Unittest/test.wav',
            name = 'Melody 1',
            status = 'Uploaded',
            pdf = ' pdf/test.pdf '

        )



    def test_name_label(self):
        melody = Melody.objects.get(id=1)
        field_label = melody._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название мелодии')

    def test_name_max_length(self):
        melody = Melody.objects.get(id=1)
        max_length = melody._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_str_is_name(self):
        melody = Melody.objects.get(id=1)
        expected_object_name = melody.name
        self.assertEquals(expected_object_name, str(melody))


