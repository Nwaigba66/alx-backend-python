#!/usr/bin/env python3
"""This module define the async_generator coroutine function
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates 10 random numbers
    """
    for count in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
