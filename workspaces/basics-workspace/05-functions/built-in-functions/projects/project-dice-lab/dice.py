"""Dice Lab.

A fair six-sided die shows each face from 1 to 6 with the same chance. The functions below roll the
die and count the results; display.py draws the die and a bar chart of the counts.
"""
import random


def average(counts):
    """Return the mean face of the rolls in counts, a dictionary {face: number of rolls}."""
    rolls = sum(counts.values())
    if rolls == 0:
        return 0
    total = 0
    for face, number in counts.items():
        total += face * number
    return total / rolls


# Task 1 - Complete
# Return the result of one roll of a fair six-sided die: a whole number from 1 to 6.
def roll():
    # TODO: use a function from the random module.
    return 1


# Task 2 - Correct the AI code
# An assistant might answer the request "Write count_rolls(n): roll a die n times and count each face" like this.
# Simulate 1,000 rolls and look at the chart, then find and fix the mistake.
def count_rolls(n):
    """Roll a die n times and return a dictionary {face: count} for the faces 1 to 6."""
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(n):
        face = random.randint(1, 5)
        counts[face] += 1
    return counts


# Task 3 - Extend (optional)
# Roll two dice n times and return a dictionary {total: count} for the totals 2 to 12.
# While this function returns None, the Two dice button stays hidden.
def count_totals(n):
    # TODO: your simulation of two dice
    return None
