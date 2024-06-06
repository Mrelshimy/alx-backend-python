#!/usr/bin/env python3
""" sum_mixed_list module """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum_mixed_list function
    """
    sum = 0
    for i in mxd_lst:
        if isinstance(i, (float, int)):
            sum += i
    return sum
