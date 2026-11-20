# Worked examples from Double-Ended Queues with `deque`.
# Run from a separate practice folder.

from collections import deque

tasks = deque(["task1", "task2"])
tasks.append("task3")      # add to right
tasks.appendleft("urgent") # add to left
print(tasks)

tasks.pop()       # remove "task3"
tasks.popleft()   # remove "urgent"
print(tasks)
