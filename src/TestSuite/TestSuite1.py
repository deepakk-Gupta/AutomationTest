'''
Created on Apr 24, 2016

@author: Deepak_Gupta
'''
import unittest
import sys
from TestCases.Test2 import testcases1

class TestSuite1(unittest.TestSuite):
           def __init__(self):
               unittest.TestSuite.__init__(self,map(testcases1,
                                                     ("test_case3",
                                                      "test_case4")))