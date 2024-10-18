#!/usr/bin/env python3
"""
You will spawn wait_random n times with the specified max_delay
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait_n should return the list of all the delays (float values)

    Args:
        n(int): times of spawn
        max_delay(int): maximum amount of delay in second

    Returns:
        delay(list[float]): List of the delays in ascending order
    """
    delays = []

    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
