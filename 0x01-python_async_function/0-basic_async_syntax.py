#!/usr/bin/env python3
"""This module define the wait_random subroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random value between 0 and max_delay

    Arguments:
    =========
    max_delay - maximum seconds to delay

    Returns - random generated delay
    """

    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
