# Worked examples from Threads: Best for I/O-Bound Tasks.
# Run from a separate practice folder.

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def fake_fetch(url, delay=0.2):
    """Simulate a slow network request by sleeping briefly."""
    time.sleep(delay)
    return f"OK {url} ({delay:.1f}s)"

urls = [f"https://example.org/page/{i}" for i in range(5)]

start = time.perf_counter()

# Create a pool of threads
with ThreadPoolExecutor(max_workers=5) as pool:
    # Schedule each fetch in its own thread
    futures = [
        pool.submit(fake_fetch, u, 0.2 + (i % 3) * 0.1)
        for i, u in enumerate(urls)
    ]
    # Print results as they finish
    for fut in as_completed(futures):
        print(fut.result())

elapsed = time.perf_counter() - start
print(f"Total time ~ {elapsed:.2f}s (overlapping waits)")
