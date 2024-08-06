#!/usr/bin/env python3
"""
This module writes a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
"""


import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
