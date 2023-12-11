#!/usr/bin/env python3
"""This module define a coroutine that call another coroutine n times
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the wait_random n times

    Arguments:
    =========
    n - number of calls of wait_random
    max_delay - maximum delay per call of wwit_random
    Returns - List of wait time for all calls
    """
    queue = []
    for task in asyncio.as_completed(
            [wait_random(max_delay) for idx in range(n)]):
        ans = await task
        queue.append(ans)
    return queue
