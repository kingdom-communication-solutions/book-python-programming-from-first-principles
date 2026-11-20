"""Library stage 08: Book and Catalogue protect their own rules."""


class Book:
    loan_days = 14
    created_count = 0

    def __init__(self, copy_id, title, author, year):
        self.copy_id = copy_id
        self.title = title
        self.author = author
        self.year = year
        self._available = True
        Book.created_count += 1

    @classmethod
    def from_record(cls, record):
        copy_id, title, author, year = record.split(";")
        return cls(copy_id, title, author, int(year))

    @staticmethod
    def is_valid_copy_id(copy_id):
        return len(copy_id) == 4 and copy_id[0] == "B" and copy_id[1:].isdigit()

    @property
    def available(self):
        return self._available

    def description(self):
        return f"{self.title} by {self.author} ({self.year})"

    def check_out(self):
        if not self._available:
            raise ValueError(f"{self.copy_id} is already on loan")
        self._available = False

    def check_in(self):
        if self._available:
            raise ValueError(f"{self.copy_id} is not on loan")
        self._available = True


class Catalogue:
    def __init__(self):
        self._books = {}

    def add(self, book):
        if not Book.is_valid_copy_id(book.copy_id):
            raise ValueError(f"Invalid copy ID: {book.copy_id}")
        if book.copy_id in self._books:
            raise ValueError(f"Duplicate copy ID: {book.copy_id}")
        self._books[book.copy_id] = book

    def find(self, copy_id):
        return self._books.get(copy_id)

    def by_author(self, author):
        return [book.title for book in self._books.values() if book.author == author]

    def available_titles(self):
        return [book.title for book in self._books.values() if book.available]


catalogue = Catalogue()
for record in [
    "B001;River Stories;A. Mensah;2024",
    "B002;Silent Maps;L. Chen;2021",
]:
    catalogue.add(Book.from_record(record))

river = catalogue.find("B001")
river.check_out()
print(river.available)

try:
    river.check_out()
except ValueError as error:
    print("Refused:", error)

try:
    catalogue.add(Book("B002", "Silent Maps", "L. Chen", 2021))
except ValueError as error:
    print("Refused:", error)

print(catalogue.available_titles())
