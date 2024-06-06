#!/usr/bin/env python3
""" multiplier module """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplier function
    """
    def func(float):
        return multiplier * float
    return func
