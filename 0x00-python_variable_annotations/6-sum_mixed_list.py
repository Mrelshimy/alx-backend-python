#!/usr/bin/env python3
""" sum list module with annotations """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """sum_mixed_list function"""

    sum = 0
    for item in mxd_list:
        sum += item
    return sum
