"""Museum Collection Explorer: the 4,693 paintings of the Cleveland Museum of Art.

Data: Cleveland Museum of Art, Open Access metadata (CC0 1.0), snapshot of 3 November 2026.
"""
import csv
from collections import Counter, defaultdict

DATA = "cma-paintings.csv"


def load_paintings(path):
    """Return the records of the CSV file as dictionaries; the two year columns become integers, or None if empty."""
    with open(path, encoding="utf-8", newline="") as file:
        records = list(csv.DictReader(file))
    for record in records:
        for key in ("earliest_year", "latest_year"):
            record[key] = int(record[key]) if record[key] else None
    return records


# Task 2 - Correct the AI code
# An assistant might answer the request "Write century(year): 19 for the years 1801 to 1900, 20 for 1901 to 2000,
# and negative centuries for years before the Common Era, such as -3 for 300 BCE" like this.
# Run the tests in test_museum.py, then find and fix the mistake.
def century(year):
    """Return the century of a year: 19 for 1801 to 1900, -1 for 100 BCE to 1 BCE."""
    return year // 100 + 1


# Task 1 - Complete
# Return a dictionary that counts the paintings per century of their earliest year, using defaultdict(int).
def paintings_per_century(records):
    counts = defaultdict(int)
    # TODO: one loop over the records
    return counts


def label(number):
    """Return a century as text: 19 becomes "19th", -3 becomes "3rd BCE"."""
    n = abs(number)
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}" + (" BCE" if number < 0 else "")


def report(records):
    print(f"{len(records):,} paintings")
    print()
    print("Largest departments:")
    for department, count in Counter(r["department"] for r in records).most_common(5):
        print(f"  {count:5}  {department}")
    print()
    print("Paintings per century of their earliest year (# = 25 paintings):")
    counts = paintings_per_century(records)
    for number in sorted(counts):
        bar = "#" * round(counts[number] / 25)
        print(f"  {label(number):>9} {counts[number]:5} {bar}".rstrip())
    print()
    named = [r["artists"] for r in records if r["artists"].strip()]
    print(f"Without a named artist: {len(records) - len(named):,} ({(len(records) - len(named)) / len(records):.1%})")
    print("Most frequent artists:")
    for artist, count in Counter(named).most_common(3):
        print(f"  {count:3}  {artist}")


if __name__ == "__main__":
    report(load_paintings(DATA))
