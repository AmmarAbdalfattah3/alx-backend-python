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
    Measures the runtime of executing async_comprehension

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    tasks = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
