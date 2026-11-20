# Worked examples from Iteration Tools with `itertools`.
# Run from a separate practice folder.

from itertools import combinations

students = ["Ada", "Grace", "Alan"]

for pair in combinations(students, 2):
    print(pair)

from itertools import permutations

letters = ["A", "B", "C"]

for p in permutations(letters, 2):
    print(p)

from itertools import product

learning_rates = [0.01, 0.1]
batch_sizes = [16, 32]

for combo in product(learning_rates, batch_sizes):
    print(combo)

from itertools import chain

group1 = ["Ada", "Grace"]
group2 = ["Alan"]
group3 = ["Linus", "Margaret"]

for name in chain(group1, group2, group3):
    print(name)
