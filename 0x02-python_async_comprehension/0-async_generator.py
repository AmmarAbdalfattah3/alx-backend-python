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
    Asynchronous generator that yields random numbers.

    This coroutine asynchronously generates 10 random floating-point numbers.
    It waits for 1 second between each generation.

    Yields:
        float: A random floating-point number between 0 and 10.

    Example:
        async for number in async_generator():
            print(number)
    """
    count = 0
    while count < 10:
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.random() * 10  # Yield a random number between 0 and 10
        count += 1
