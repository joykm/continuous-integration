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


if __name__ == '__main__':
    unittest.main()
