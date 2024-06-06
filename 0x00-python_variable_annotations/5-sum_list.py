#!/usr/bin/env python3
""" sum list module with annotations """


def sum_list(input_list: list[float]) -> float:
    """sum_list function"""

    sum = 0
    for item in input_list:
        sum += item
    return sum
