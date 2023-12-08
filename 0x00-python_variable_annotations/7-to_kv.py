#!/usr/bin/env python3
"""This module define a function with complex type notation
"""
from typing import Union, Tuple

Number = Union[int, float]

ReturnType = Tuple[str, float]


def to_kv(k: str, v: Number) -> ReturnType:
    """Square the number

    Arguments:
    =========
    k (string) - first argument representing key
    v (number) - second argument as value

    Return (tuple) - (k, square of number as float)
    """
    return (k, v * v)
