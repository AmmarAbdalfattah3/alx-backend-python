#!/usr/bin/env python3
"""
The module creates a measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
