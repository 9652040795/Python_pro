import unittest
from funniest import joke,fact,div

class TestFunny(unittest.TestCase):
    def test_joke(self):
        got_joke=joke()
        self.assertTrue(isinstance(got_joke,basestring))

    def test_fact(self):
        res = fact(5)
        self.assertEqual(res, 120)

    def test_error(self):
        self.assertRaises(ZeroDivisionError, div, 0)


if __name__ == '__main__':
    unittest.main()
