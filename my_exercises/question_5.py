#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 5
# Level 1
#
################################################################
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters
#
################################################################

class Foo(object):

    def __init__(self):
        self.string: str = ''
    
    def getString(self):
        self.string = input('input string: ')
    
    def printString(self):
        print(self.string.upper())

if __name__ == '__main__':
    foo: Foo = Foo()
    foo.getString()
    foo.printString()