import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    # function 2 unit tests
    def test1_func2(self):
        input = "1234"
        self.assertTrue(conv_num(input) == 1234)


if __name__ == '__main__':
    unittest.main()
