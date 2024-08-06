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
    An asynchronous generator that yields 10 random float numbers.

    This coroutine asynchronously waits for 1 second in each iteration and
    then yields a random number within the specified range.

    Yields:
        float: A random number between 0 and 10.

    Example:
        async for number in async_generator():
            print(number)
    """
    async for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
