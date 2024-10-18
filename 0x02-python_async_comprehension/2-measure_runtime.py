#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n, max_delay)
"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure_time function with integers n and max_delay as arguments

    Args:
        n(int): times of spawn
        max_delay(int): maximum amount of delay in second

    Returns:
        returns total_time / n
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start = time.time()
    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - start
    return total_time / n
