"""Library stage 07: a Catalogue object manages a collection of Book objects."""


class Book:
    loan_days = 14
    created_count = 0

    def __init__(self, copy_id, title, author, year):
        self.copy_id = copy_id
        self.title = title
        self.author = author
        self.year = year
        self.available = True
        Book.created_count += 1

    @classmethod
    def from_record(cls, record):
        copy_id, title, author, year = record.split(";")
        return cls(copy_id, title, author, int(year))

    @staticmethod
    def is_valid_copy_id(copy_id):
        return len(copy_id) == 4 and copy_id[0] == "B" and copy_id[1:].isdigit()

    def description(self):
        return f"{self.title} by {self.author} ({self.year})"

    def check_out(self):
        if not self.available:
            return False
        self.available = False
        return True

    def check_in(self):
        self.available = True


class Catalogue:
    def __init__(self):
        self.books = []

    def add(self, book):
        if self.find(book.copy_id) is not None:
            return False
        self.books.append(book)
        return True

    def find(self, copy_id):
        for book in self.books:
            if book.copy_id == copy_id:
                return book
        return None

    def by_author(self, author):
        return [book.title for book in self.books if book.author == author]

    def available_titles(self):
        return [book.title for book in self.books if book.available]


catalogue = Catalogue()
for record in [
    "B001;River Stories;A. Mensah;2024",
    "B002;Silent Maps;L. Chen;2021",
    "B003;City Letters;K. Owusu;2019",
    "B005;Harbour Songs;A. Mensah;2022",
]:
    catalogue.add(Book.from_record(record))

print(catalogue.add(Book("B002", "Silent Maps", "L. Chen", 2021)))
print(len(catalogue.books))
print(catalogue.find("B003").description())
print(catalogue.find("B999"))
print(catalogue.by_author("A. Mensah"))

catalogue.find("B001").check_out()
print(catalogue.available_titles())
