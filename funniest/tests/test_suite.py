import unittest
from funniest import joke,fact,div

class TestSuiteFunny(unittest.TestCase):
    def test_joke(self):
        got_joke=joke()
        self.assertTrue(isinstance(got_joke,basestring))

    def test_fact(self):
        res = fact(5)
        self.assertEqual(res, 120)

    def test_error(self):
        self.assertRaises(ZeroDivisionError, div, 0)


def suite(self):
    suite= unittest.TestSuite()
    suite.addTest(TestSuiteFunny())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite=suite()
    runner.run(test_suite)

    #unittest.main()

