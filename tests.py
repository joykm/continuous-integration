import unittest
from task import conv_num
from task import conv_endian
from task import my_datetime
from datetime import datetime


class TestCase(unittest.TestCase):

    # Function 1
    # test that an integer string returns as an integer
    def test1_func1(self):
        """test that an integer string returns as an integer"""
        str_num = "1234"
        self.assertTrue(conv_num(str_num) == 1234)

    # test that a float string returns as a float
    def test2_func1(self):
        """test that a float string returns as a float"""
        str_num = "1234.12"
        self.assertTrue(conv_num(str_num) == 1234.12)

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

    # test that negative number returns negative number
    def test5_func1(self):
        """test that negative number returns negative number"""
        str_num = "6.-50"
        self.assertEqual(conv_num(str_num), None)

    # test for allowed character
    def test6_func1(self):
        """test that non allowed character found returns false"""
        str_num = "*138.12"
        self.assertEqual(conv_num(str_num), None)

    # test for repeat '0x' in hexadecimal input string
    def test7_func1(self):
        """repeated 0x in hexadecimal returns None"""
        str_num = "0xA0x"
        self.assertEqual(conv_num(str_num), None)

    # test for repeat '0X' in hexadecimal input string
    def test8_func1(self):
        """repeated 0X in hexadecimal returns None"""
        str_num = "0XA0X"
        self.assertEqual(conv_num(str_num), None)

    # test for hexadecimal conversion
    def test9_func1(self):
        """test 0xAD4  should return decimal 2772"""
        str_num = "0xAD4"
        self.assertEqual(conv_num(str_num), 2772)

    # test for hexadecimal conversion with negative input string
    def test10_func1(self):
        """test -0xAD4  should return decimal -2772"""
        str_num = "-0xAD4"
        self.assertEqual(conv_num(str_num), -2772)

    # test for hexadecimal conversion with unexpected character
    def test11_func1(self):
        """hexadecimal 0xAG5 has 'G' which is not Hexadecimal symbol returns None"""
        str_num = "0xAG5"
        self.assertEqual(conv_num(str_num), None)

    # test for hexadecimal conversion
    def test12_func1(self):
        """test 0XAD5  should return decimal 2772"""
        str_num = "0XAD4"
        self.assertEqual(conv_num(str_num), 2772)

    # test for hexadecimal conversion with unexpected character
    def test13_func1(self):
        """hexadecimal 0xAX5 has 'G' which is not Hexadecimal letter returns None"""
        str_num = "0xAX5"
        self.assertEqual(conv_num(str_num), None)

    # test for mixed decimal and hexadecimal string input
    def test14_func1(self):
        """mixed number and letter that not start with 0x or 0X return None"""
        str_num = "126A"
        self.assertEqual(conv_num(str_num), None)

    # test for repeat '.' in input string
    def test15_func1(self):
        """input string repeat '.' returns None"""
        str_num = "12.2.3"
        self.assertEqual(conv_num(str_num), None)

    # Function 2
    # test 01-01-1970 start of day matches datetime
    def test1_func2(self):
        """test 01-01-1970 start of day matches datetime"""
        num_sec = 0
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # test 01-01-1970 end of day matches datetime
    def test2_func2(self):
        """test 01-01-1970 end of day matches datetime"""
        num_sec = 86399
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # test 03-01-1970 start of day matches datetime
    def test3_func2(self):
        """test 03-01-1970 start of day matches datetime"""
        num_sec = 5097600
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # test 02-29-1972 start of day matches datetime
    def test4_func2(self):
        """test 02-29-1972 start of day matches datetime"""
        num_sec = 68169600
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # test 11-29-1973 (class example)
    def test5_func2(self):
        """test 11-29-1973 (class example)"""
        num_sec = 123456789
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # test 12-22-2282 (class example)
    def test6_func2(self):
        """test 12-22-2282 (class example)"""
        num_sec = 9876543210
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # 02-29-8360 (class example)
    def test7_func2(self):
        """02-29-8360 (class example)"""
        num_sec = 201653971200
        self.assertEqual(my_datetime(num_sec), datetime.utcfromtimestamp(num_sec).strftime("%m-%d-%Y"))

    # Fuction 3
    # Should be 0E 91 A2 (class example)
    def test1_func3(self):
        """Expected result is 0E 91 A2 (class example)"""
        # fix this when the function is working
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test2_func3(self):
        """Test for negative number handling. Expected -0E 91 A2 (class example)"""
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test3_func3(self):
        """Test for little endian. Expected: A2 91 0E (class example)"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test4_func3(self):
        """Test for negative little endian. Expected: -A2 91 0E (class example)"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test5_func3(self):
        """Test that explicit parameter invocations are accepted (class example)"""
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test6_func3(self):
        """Test that invalid second parameter returns None (class example)"""
        self.assertEqual(conv_endian(num=-955786, endian='small'), None)


if __name__ == '__main__':
    unittest.main()
