#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 3
# Level 1
#
################################################################
#
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()
#
################################################################

from functools import reduce
from typing import Dict

input_str: str = input('input an integer: ')

n: int = int(input_str)
result: Dict = {}
for i in range(1, n+1):
    result[i] = i * i
print(result)
