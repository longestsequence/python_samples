import unittest
from utils import check_if_even
class TestEven(unittest.TestCase):

    def test1(self):
        assert check_if_even(2)
