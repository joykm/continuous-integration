import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    # test that an integer string returns as an integer
    def test1_func1(self):
        """test that an integer string returns as an integer"""
        input = "1234"
        self.assertTrue(conv_num(input) == 1234)

    # test that a float string returns as a float
    def test2_func1(self):
        """test that a float string returns as a float"""
        input = "1234.12"
        self.assertTrue(conv_num(input) == 1234.12)

    # test that empty string returns None
    def test3_func1(self):
        """test that empty string returns None"""
        str_num = ''
        self.assertEqual(conv_num(str_num), None)

    # test that negative number returns negative number
    def test4_func1(self):
        """test that negative number returns negative number"""
        str_num = "-6.50"
        self.assertEqual(conv_num(str_num), -6.50)

    # test number start with "."
    def test5_func1(self):
        """test that number started with "." will return in proper format"""
        str_num = ".45"
        self.assertEqual(conv_num(str_num), 0.45)

    # test number end with "."
    def test6_func1(self):
        """test that number end with "." returns in proper format"""
        str_num = "123."
        self.assertEqual(conv_num(str_num), 123.0)


if __name__ == '__main__':
    unittest.main()
