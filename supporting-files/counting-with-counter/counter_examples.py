# Worked examples from Counting with `Counter`.
# Run from a separate practice folder.

from collections import Counter

text = "to be or not to be that is the question"
counts = Counter(text.split())

print(counts)
print(counts.most_common(2))

errors = ["500", "404", "404", "503", "500", "500"]
print(Counter(errors))
