#!/usr/bin/env python3
""" Max delay module"""
import asyncio
import random


async def wait_random(max_delay=10):
    """ Max Delay function

        Args: wait_random, the value to delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
