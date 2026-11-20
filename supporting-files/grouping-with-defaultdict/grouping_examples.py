# Worked examples from Grouping with `defaultdict`.
# Run from a separate practice folder.

from collections import defaultdict

words = ["cat", "apple", "dog", "pear", "bee"]
groups = defaultdict(list)

for w in words:
    groups[len(w)].append(w)

print(groups)
