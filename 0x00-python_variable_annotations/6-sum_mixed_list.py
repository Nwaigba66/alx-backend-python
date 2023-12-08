#!/usr/bin/env python3
"""This module define a function that take a list of numbers and return the sum
"""
from typing import List, Union

Number = Union[int, float]

ListOfNumbers = List[Number]


def sum_mixed_list(mxd_lst: ListOfNumbers) -> float:
    """Add all items in mxd_lst

    Arguments:
    =========
    mxd_lst (list of float): list of numbers to sum

    Returns - (float) sum of all items in the list
    """
    if len(mxd_lst) == 1:
        return mxd_lst[0]
    item, *remaining = mxd_lst
    return float(item + sum_mixed_list(remaining))
