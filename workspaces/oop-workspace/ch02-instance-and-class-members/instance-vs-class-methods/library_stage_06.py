"""Library stage 06: a class method builds books from text records; a static method checks copy IDs."""


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


records = [
    "B001;River Stories;A. Mensah;2024",
    "B002;Silent Maps;L. Chen;2021",
    "B003;City Letters;K. Owusu;2019",
]
books = [Book.from_record(record) for record in records]

for book in books:
    print(book.copy_id, book.description())

print(Book.is_valid_copy_id("B004"))
print(Book.is_valid_copy_id("4"))
print("Books created:", Book.created_count)
