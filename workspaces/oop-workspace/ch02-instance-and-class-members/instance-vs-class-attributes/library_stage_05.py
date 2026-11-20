"""Library stage 05: a shared loan period and a count of created books."""


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

    def description(self):
        return f"{self.title} by {self.author} ({self.year})"

    def check_out(self):
        if not self.available:
            return False
        self.available = False
        return True

    def check_in(self):
        self.available = True


river = Book("B001", "River Stories", "A. Mensah", 2024)
maps = Book("B002", "Silent Maps", "L. Chen", 2021)

print(Book.loan_days, river.loan_days, maps.loan_days)
print("Books created:", Book.created_count)

Book.loan_days = 21
print(river.loan_days, maps.loan_days)
