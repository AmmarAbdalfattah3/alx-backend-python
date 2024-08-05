#!/usr/bin/env python3
"""
This module writes an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    the list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)
    return sorted_delays
