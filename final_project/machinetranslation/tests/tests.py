import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")
    
    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

    def test_null_input_e2f(self):
        self.assertIsNotNone(english_to_french(None))

    def test_null_input_f2e(self):
        self.assertIsNotNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()