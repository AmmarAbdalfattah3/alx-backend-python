#!/usr/bin/env python3
"""
The module writes a function (do not create an async function,
use the regular function syntax to do this) task_wait_random that
takes an integer max_delay and returns a asyncio.Task.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.
    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.
    Returns:
        asyncio.Task: An asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
