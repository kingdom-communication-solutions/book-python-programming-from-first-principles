# Worked examples from Lightweight Records with `namedtuple`.
# Run from a separate practice folder.

from collections import namedtuple

Location = namedtuple("Location", ["city", "lat", "lon"])
paris = Location("Paris", 48.8566, 2.3522)

print(paris.city, paris.lat)

Person = namedtuple("Person", ["name", "age", "city"])
records = [
    Person("Alice", 30, "Berlin"),
    Person("Bob", 25, "Munich"),
]

print("Name       | Age | City")
print("-" * 28)
for r in records:
    print(f"{r.name:<10} | {r.age:<3} | {r.city}")
