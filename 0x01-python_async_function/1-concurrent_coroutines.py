#!/usr/bin/env python3
""" Max delay module """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times and return sorted list of values"""

    list = []
    tasks = [wait_random(max_delay) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        list.append(delay)
    return list
