#!/usr/bin/env python3
"""This module define a function that take a list of numbers and return the sum
"""
from typing import List

ListOfFloat = List[float]


def sum_list(input_list: ListOfFloat) -> float:
    """Add all items in input_list

    Arguments:
    =========
    input_list (list of float): list of numbers to sum

    Returns - (float) sum of all items in the list
    """
    if len(input_list) == 1:
        return input_list[0]
    item, *remaining = input_list
    return item + sum_list(remaining)
