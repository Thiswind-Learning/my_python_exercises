#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 2
# Level 1
#
################################################################
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

from functools import reduce

input_str: str = input('input an integer: ')

n: int = int(input_str)
result: int = reduce(lambda a, b: a * b, range(1, n+1))

print(result)