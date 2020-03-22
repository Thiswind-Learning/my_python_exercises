#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def main():
    r"""
    Question 5
     
    Level 1
    
    Question:
    Define a class named Foo which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    

    Test:
    >>> from unittest.mock import patch
    >>> from io import StringIO
    >>> import sys
    >>> user_input = ['ABC 123']
    >>> with patch('builtins.input', side_effect=user_input):
    ...     obj = Foo()
    ...     obj.getString()
    ...     old_out = sys.stdout
    ...     out = StringIO()
    ...     sys.stdout = out
    ...     obj.printString()
    ...     sys.stdout = old_out
    ... 
    >>> out.getvalue().strip()
    'ABC 123'
    
    """
    pass

#### Your code below

#### Your code above


if __name__ == '__main__':
    main()
