# Worked examples from Priority Queues with `heapq`.
# Run from a separate practice folder.

import heapq

# (priority, description)
tasks = [
    (3, "Update documentation"),
    (1, "Fix production bug"),
    (2, "Reply to customer emails"),
]

heapq.heapify(tasks)  # turn list into a heap

while tasks:
    priority, description = heapq.heappop(tasks)
    print(f"Handling (priority {priority}): {description}")

import heapq

errors = [0.42, 0.15, 0.78, 0.05, 0.33]
best = heapq.nsmallest(2, errors)
print(best)
