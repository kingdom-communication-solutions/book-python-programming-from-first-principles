# Worked examples from File Serialization.
# Run from a separate practice folder.

import csv

rows = [
    ["id", "title", "year"],
    [1, "Hamlet", 1603],
    [2, "Macbeth", 1606],
]

with open("plays.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("plays.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv

with open("plays.csv", "r", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["title"], int(row["year"]))

import json

book = {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "year": 1813,
    "characters": ["Elizabeth Bennet", "Mr. Darcy"]
}

with open("book.json", "w", encoding="utf-8") as f:
    json.dump(book, f)

with open("book.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)

import pickle

numbers = {"evens": [2, 4, 6], "odds": [1, 3, 5]}

with open("numbers.pkl", "wb") as f:
    pickle.dump(numbers, f)

with open("numbers.pkl", "rb") as f:
    restored = pickle.load(f)

print(restored)

from pathlib import Path

base = Path(".")           # current directory
data_dir = base / "data"   # build a subdirectory path
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "hello.txt"
file_path.write_text("Hello from pathlib!", encoding="utf-8")

print(file_path.read_text(encoding="utf-8"))
