#!/usr/bin/env python3
""" element length module """


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element length function
    """
    return [(i, len(i)) for i in lst]

