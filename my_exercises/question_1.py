#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 1
# Level 1
#
################################################################
#
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints: 
# Consider use range(#begin, #end) method
#
################################################################

from typing import List
from functools import reduce

result: List[int] = [x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
output_str: str = reduce(lambda a, b: f'{a}, {b}', result)
print(output_str)