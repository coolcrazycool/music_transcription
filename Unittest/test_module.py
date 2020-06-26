import unittest

from app_code.WAVconverter import audio_analyzer


class TestMelodyModule(unittest.TestCase):
    def test_allow_format(self):
        self.assertEqual([[49, 10]], audio_analyzer('./Unittest/test.wav'))

    def test_disallow_format(self):
        self.assertRaises(ValueError, audio_analyzer, './Unittest/test.mp3')

    def test_allow_music_file(self):
        self.assertEqual([[49, 10]], audio_analyzer('./Unittest/test.wav'))

    def test_disallow_music_file(self):
        self.assertRaises(ValueError, audio_analyzer, './Unittest/test_none.wav')

