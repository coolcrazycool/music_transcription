from django.test import TestCase
from music_api.forms import MelodyForm

class TestModels(TestCase ):


    def test_melody_form_blank_data(self):
        form = MelodyForm()
        self.assertFalse(form.is_valid())

    '''
    def test_melody_form_correct_data(self):
        data = {
            'user': '',
            'melody': 'test',
            'name': 'test',
            'status': 'Uploaded'}
        form = MelodyForm(data)
        print(form.errors.as_data())
        #self.assertTrue(form.is_valid())
    '''

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
