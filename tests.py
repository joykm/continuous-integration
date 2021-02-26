import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    # test that an integer string returns as an integer
    def test1_func1(self):
        input = "1234"
        self.assertTrue(conv_num(input) == 1234)

    # test that a float string returns as a float
    def test2_func1(self):
        input = "1234.12"
        self.assertTrue(conv_num(input) == 1234.12)


if __name__ == '__main__':
    unittest.main()
