#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""


import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random floating-point numbers.

    This coroutine asynchronously generates 10 random floating-point numbers.
    It pauses for 1 second between each number generation.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
