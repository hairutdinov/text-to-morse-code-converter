from unittest import TestCase
from morse import Morse


class MorseTest(TestCase):
    def test_encoded(self):
        tests = {
            'hello world!': '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--',
            'Lorem ipsum dolor sit amet.':
                '.-.. --- .-. . -- / .. .--. ... ..- -- / -.. --- .-.. --- .-. / ... .. - / .- -- . - .-.-.-',
            '1234567890': '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----',
        }
        for text, expected in tests.items():
            self.assertEqual(Morse.encode(text), expected)

    def test_decode(self):
        tests = {
            '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--': 'HELLO WORLD!',
            '.-.. --- .-. . -- / .. .--. ... ..- -- / -.. --- .-.. --- .-. / ... .. - / .- -- . - .-.-.-':
                'LOREM IPSUM DOLOR SIT AMET.',
            '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----': '1234567890',
        }
        for encoded, expected in tests.items():
            self.assertEqual(Morse.decode(encoded), expected)
