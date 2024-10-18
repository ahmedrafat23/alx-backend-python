#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    """Coroutine that loops 10 times, waits for 1 second, and yields a random number."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

