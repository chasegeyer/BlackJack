import unittest
import cap


#you will inheret from unittest the class TestCase
class TestCap(unittest.TestCase):

    # crate a function for each test
    def test_one_word(self):
        # going to test cap_text function you need to test with criteria (text = 'python')
        # make sure you function performs as expected
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()