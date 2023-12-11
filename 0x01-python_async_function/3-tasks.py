#!/usr/bin/env python3
"""This module define a function that create an async task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio Task
    """
    return asyncio.Task(wait_random(max_delay))
