#!/usr/bin/env python3
"""
This module defines the task_wait_n coroutine that takes in
2 int arguments:n and max_delay. You will spawn task_wait_random n times with
the specified max_delay.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and return
    the list of all the delays in ascending order.
    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
