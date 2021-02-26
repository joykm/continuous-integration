import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    # function 1 unit tests
    def test1_func1(self):
        input = "1234"
        self.assertTrue(conv_num(input) == 1234)


if __name__ == '__main__':
    unittest.main()
