#!/usr/bin/env python3
"""This module define a function that measure runtikr of fou coroutines
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure tike taken to run 4 coroutines
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()))
    return time.perf_counter() - start_time
