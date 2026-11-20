"""Letters Archive: find the dates in six letters and list them in date order."""
import datetime
import re
from letters import LETTERS

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def place_of(letter):
    """Return the place on the second line, the text before the comma."""
    return letter.splitlines()[1].split(",")[0]


def writer_of(letter):
    """Return the writer's name, the last line of the letter."""
    return letter.splitlines()[-1]


# Task 1 - Complete
# Write a pattern with three groups for dates such as "14 March 1851": the day (one or two digits),
# the month (a capital letter followed by lowercase letters) and the year (four digits).
DATE = r""   # TODO


def date_of(letter):
    """Return the first date in the letter as a datetime.date, or None if there is none."""
    found = re.search(DATE, letter)
    if found is None or found.group(0) == "":
        return None
    day, month, year = found.groups()
    return datetime.date(int(year), MONTHS.index(month) + 1, int(day))


# Task 2 - Correct the AI code
# An assistant might answer the request "Write year_of(letter): return the year in which the letter was written" like this.
# Look at the years in the summary, then find and fix the mistake.
def year_of(letter):
    """Return the year of the letter as an integer."""
    return int(re.search(r"\d{4}", letter).group())


# Task 3 - Extend (optional)
# Return a dictionary that counts the letters written in each place, such as {"Bristol": 2, ...}.
def letters_per_place(letters):
    # TODO
    return None


if __name__ == "__main__":
    print("Letters in date order:")
    dated = [letter for letter in LETTERS if date_of(letter) is not None]
    if not dated:
        print("  no dates found yet (complete Task 1)")
    for letter in sorted(dated, key=date_of):
        print(f"  {date_of(letter).strftime('%d %B %Y'):<18}{place_of(letter):<10} {writer_of(letter)}")
    print()
    print("Letters per year:")
    years = {}
    for letter in LETTERS:
        year = year_of(letter)
        years[year] = years.get(year, 0) + 1
    for year in sorted(years):
        print(f"  {year}: {'#' * years[year]}")
    places = letters_per_place(LETTERS)
    if places is not None:
        print()
        print("Letters per place:")
        for place in sorted(places):
            print(f"  {place}: {places[place]}")
