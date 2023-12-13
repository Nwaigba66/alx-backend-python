#!/usr/bin/env python3
"""This module define a coroutine that create list of random numbers
using async comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return list of 10 random number with comprehension
    """
    return [i async for i in async_generator()]
