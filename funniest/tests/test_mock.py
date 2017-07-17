from unittest import TestCase
from mock import patch



class TestFunniest(TestCase):
    @patch('funniest.calculationutilities.sum',return_value=9)
    def test_sum(self,sum):
        self.assertEquals(sum(2,3),9)

