#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Jassem Alhaj Tamer
@Student ID: 10168910
"""
from calculator import *
import unittest

class MyTest(unittest.TestCase):
    
     def testAaMenu(self):
         self.assertEqual(show_menu(),None)  
     def testAdd(self):
         self.assertEqual(sum(),None)
     def testSubstraction(self):
         self.assertEqual(sub(),None)   
     def testMultiplication(self):
         self.assertEqual(mult(),None)
     def testDivision(self):
         self.assertEqual(div(),None)
     def testModulus(self):
         self.assertEqual(modu(),None)
     def testExponential(self):
         self.assertEqual(expo(),None)
     def testFactorial(self):
         self.assertEqual(fact(),None)
     def testSquareRoor(self):
         self.assertEqual(sqr(),None)
     def testCubeRoor(self):
         self.assertEqual(cube(),None)
     def testSine(self):
         self.assertEqual(sin(),None)
  
         
         
if __name__ == '__main__':
    unittest.main()