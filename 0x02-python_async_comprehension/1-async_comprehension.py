#!/usr/bin/env python3
"""
This module writes a coroutine called async_comprehension
that takes no arguments.
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""


import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Collects 10 random numbers using asynchronous comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [num async for num in async_generator()]
