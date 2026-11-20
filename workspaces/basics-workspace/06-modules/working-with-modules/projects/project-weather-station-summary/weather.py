"""Weather Station Summary: October in central England, 1825 and 2025."""
import statistics
from cet_october import READINGS


# Task 1 - Complete
# Return the daily mean temperatures of one year, in date order, as a list of floats.
def temperatures(year):
    # TODO: one list comprehension over READINGS that keeps the readings whose date starts with year.
    return []


# Task 2 - Correct the AI code
# An assistant might answer the request "Write median(values) without the statistics module" like this.
# Compare its result with statistics.median() for both years, then find and fix the mistake.
def median(values):
    """Return the median of a list of numbers."""
    middle = len(values) // 2
    if len(values) % 2 == 1:
        return values[middle]
    return (values[middle - 1] + values[middle]) / 2


# Task 3 - Extend (optional)
# Return the same temperatures in degrees Fahrenheit, F = C * 9 / 5 + 32, rounded to one decimal place.
def fahrenheit(values):
    # TODO: one list comprehension
    return None


def bar_chart(values):
    """Print how many days fall into each band of 5 degrees, as a row of # signs."""
    for low in range(0, 20, 5):
        days = len([t for t in values if low <= t < low + 5])
        print(f"  {low:2}-{low + 5:<2} °C | {'#' * days} {days}")


def summary(year):
    values = temperatures(year)
    if not values:
        print(f"October {year}: no readings yet (complete Task 1).")
        return
    print(f"October {year}: {len(values)} days")
    print(f"  warmest {max(values)} °C, coldest {min(values)} °C")
    print(f"  mean {statistics.mean(values):.1f} °C")
    print(f"  median {median(values)} °C (statistics.median: {statistics.median(values)} °C)")
    bar_chart(values)
    converted = fahrenheit(values)
    if converted is not None:
        print(f"  warmest {max(converted)} °F, coldest {min(converted)} °F")


if __name__ == "__main__":
    summary("1825")
    print()
    summary("2025")
