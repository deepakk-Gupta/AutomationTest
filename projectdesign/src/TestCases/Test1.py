import unittest
import sysconfig
import sys
from keywords.Keywords import KeyWord

#import Keywords
class testcases(unittest.TestCase):
    def setUp(self):
        print('start execution of test cases')
    def tearDown(self):
        print('stop execution of respectve the test cases')
    def test_case1(self):
        print('this is the first of first test case')
        KeyWord.printbyname(self)
    def test_case2(self):
        print('this is the second of second test case')
if __name__ == "__main__":
    unittest.main()