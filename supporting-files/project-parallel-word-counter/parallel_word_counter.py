# Worked examples from Project: Parallel Word Counter.
# Run from a separate practice folder.

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from collections import Counter
import re
import time

def count_file(path: Path) -> Counter:
    text = path.read_text(encoding="utf-8")
    return Counter(re.findall(r"\b\w+\b", text.lower()))

def merge(counters):
    total = Counter()
    for counter in counters:
        total.update(counter)
    return total

if __name__ == "__main__":
    demo_dir = Path("demo_corpus")
    demo_dir.mkdir(exist_ok=True)
    (demo_dir / "a.txt").write_text("To be, or not to be.\n", encoding="utf-8")
    (demo_dir / "b.txt").write_text("To be! To learn. To build.\n", encoding="utf-8")
    (demo_dir / "c.txt").write_text("Build, learn, repeat.\n", encoding="utf-8")
    files = [demo_dir / name for name in ("a.txt", "b.txt", "c.txt")]
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(count_file, files))
    total = merge(results)
    print("Top 5 words:", total.most_common(5))
    print(f"Completed in {time.perf_counter() - start:.2f}s")
