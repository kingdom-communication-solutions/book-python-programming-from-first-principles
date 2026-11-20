"""Checks for the Dice Lab tasks. Run them with:  python check_dice.py"""
import random
import dice


def seeded(seed, function, *args):
    """Call function with the random module started at a fixed seed, so every run gives the same results."""
    random.seed(seed)
    return function(*args)


def rolls(seed):
    random.seed(seed)
    return [dice.roll() for i in range(600)]


CHECKS = [
    ("Task 1: roll() returns whole numbers from 1 to 6", lambda: all(type(f) is int and 1 <= f <= 6 for f in rolls(1))),
    ("Task 1: every face from 1 to 6 appears in 600 rolls", lambda: set(rolls(2)) == {1, 2, 3, 4, 5, 6}),
    ("Task 2: count_rolls(600) counts 600 rolls", lambda: sum(seeded(3, dice.count_rolls, 600).values()) == 600),
    ("Task 2: the faces 1 to 6 are counted", lambda: set(seeded(4, dice.count_rolls, 600)) == {1, 2, 3, 4, 5, 6}),
    ("Task 2: every face appears in 600 rolls", lambda: min(seeded(5, dice.count_rolls, 600).values()) > 0),
    ("Task 2: the average of 6,000 rolls is close to 3.5", lambda: abs(dice.average(seeded(6, dice.count_rolls, 6000)) - 3.5) < 0.1),
]

OPTIONAL = [
    ("Task 3: the totals 2 to 12 are counted", lambda: set(seeded(7, dice.count_totals, 600)) == set(range(2, 13))),
    ("Task 3: count_totals(6000) counts 6,000 rolls", lambda: sum(seeded(8, dice.count_totals, 6000).values()) == 6000),
    ("Task 3: 7 is the most common total", lambda: max(seeded(9, dice.count_totals, 6000).items(), key=lambda pair: pair[1])[0] == 7),
]


def run(checks):
    passed = 0
    for name, test in checks:
        try:
            ok = test()
        except Exception as error:  # a crash in the learner's code counts as a failed check
            ok = False
            name += f"  ({type(error).__name__}: {error})"
        print(("✓ " if ok else "✗ ") + name)
        passed += ok
    return passed


if __name__ == "__main__":
    passed = run(CHECKS)
    print(f"{passed} of {len(CHECKS)} checks passed.")
    if dice.count_totals(1) is not None:
        print()
        extra = run(OPTIONAL)
        print(f"{extra} of {len(OPTIONAL)} optional checks passed.")
