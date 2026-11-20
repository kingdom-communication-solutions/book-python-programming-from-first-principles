# Worked examples from Async I/O with asyncio.
# Run from a separate practice folder.

import asyncio
import random
import time

async def async_fetch(name):
    """Simulate asynchronous I/O with asyncio.sleep()."""
    delay = 0.1 + random.random() * 0.2
    await asyncio.sleep(delay)       # Non-blocking delay
    return f"OK {name} ({delay:.2f}s)"

async def main():
    # Launch multiple coroutines at the same time
    tasks = [async_fetch(f"task-{i}") for i in range(5)]
    start = time.perf_counter()

    # Run all tasks concurrently and collect their results
    results = await asyncio.gather(*tasks)

    for r in results:
        print(r)

    elapsed = time.perf_counter() - start
    print(f"Total time ~ {elapsed:.2f}s (async I/O)")

# Start the event loop
asyncio.run(main())
