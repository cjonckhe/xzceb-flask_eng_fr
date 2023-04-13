import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(''),'') #test when no input is given null is the result
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #Test when 'Hello' input is given 'Bonjour' is the result

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''), '') #test when no input is given null is the result
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #Test when 'Bonjour' input is given 'Hello' is the result

unittest.main()