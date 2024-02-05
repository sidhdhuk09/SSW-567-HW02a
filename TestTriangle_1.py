# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import pytest

from Triangle_1 import classifyTriangle

def test_equilaterial_triangle():
    #assert classifyTriangle(3,3,3)=='Equilateral', '1,1,1 should be equilateral'
    #assert classifyTriangle(10,10,10)=='Equilateral' , '1,1,1 should be equilateral'
   assert classifyTriangle(0.1,0.1,0.1)=='Equilateral' ,'1,1,1 should be equilateral'


def test_right_triangle():
   # assert classifyTriangle(5,12,13)=='Right', '3,4,5 is a Right triangle'
    assert classifyTriangle(3,4,5)=='Right', '3,4,5 is a Right triangle'
    assert classifyTriangle(5,3,4)=='Right', '3,4,5 is a Right triangle'

def test_scalene_triangle():
    assert classifyTriangle(10,11,12)=='Scalene'

def test_isoceles_triangle():
    assert classifyTriangle(5,5,8)=='Isoceles'
    assert classifyTriangle(2,3,2)=='Isoceles'

def test_invalid_triangle():
    assert classifyTriangle(201,201,2011)=='InvalidInput'
    assert classifyTriangle(0,0,0)=='InvalidInput'
    assert classifyTriangle(0,0,100)=='InvalidInput'
    assert classifyTriangle(0,0.5,10.29)=='InvalidInput'
   # assert classifyTriangle(2,20,33)=='NotATriangle'

#import unittest

#from Triangle_1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

#class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #def testRightTriangleA(self):
        #self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

   # def testRightTriangleB(self):
       # self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    #def testEquilateralTriangles(self):
        #self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

#if __name__ == '__main__':
    #print('Running unit tests')
    #unittest.main()

