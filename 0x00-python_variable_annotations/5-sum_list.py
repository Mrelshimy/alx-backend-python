#!/usr/bin/env python3
""" sum list module with annotations """
import typing


def sum_list(input_list: typing.list[float]) -> float:
    """sum_list function"""

    sum = 0
    for item in input_list:
        sum += item
    return sum
