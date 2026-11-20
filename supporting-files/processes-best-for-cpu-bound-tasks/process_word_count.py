# Worked examples from Processes: Best for CPU-Bound Tasks.
# Run from a separate practice folder.

from concurrent.futures import ProcessPoolExecutor
from collections import Counter
import time

def count_words(words):
    return Counter(word.lower() for word in words)

def merge(counters):
    total = Counter()
    for counter in counters:
        total.update(counter)
    return total

if __name__ == "__main__":
    words = ("To be or not to be " * 20_000).split()
    chunks = [words[i:i + 20_000] for i in range(0, len(words), 20_000)]
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as pool:
        partials = list(pool.map(count_words, chunks))
    total = merge(partials)
    print(total.most_common(3))
    print(f"Finished in {time.perf_counter() - start:.2f}s")
