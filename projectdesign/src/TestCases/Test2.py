import unittest
import sysconfig
import sys
from keywords.Keywords import KeyWord

#import Keywords
class testcases1(unittest.TestCase):
    def setUp(self):
        print('start execution of second test cases')
    def tearDown(self):
        print('stop execution of respective the test cases')
    def test_case3(self):
        print('this is the first of second test case')
        KeyWord.printbyname(self)
    def test_case4(self):
        print('this is the second of second test case')
if __name__ == "__main__":
    unittest.main()