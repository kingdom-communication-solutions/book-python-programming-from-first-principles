"""Library stage 04: each copy has its own state, changed by its methods."""


class Book:
    def __init__(self, copy_id, title, author, year):
        self.copy_id = copy_id
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def description(self):
        return f"{self.title} by {self.author} ({self.year})"

    def check_out(self):
        if not self.available:
            return False
        self.available = False
        return True

    def check_in(self):
        self.available = True


copy_1 = Book("B001", "River Stories", "A. Mensah", 2024)
copy_2 = Book("B002", "River Stories", "A. Mensah", 2024)
shelf_label = copy_1

print(copy_1 is copy_2)
print(copy_1 is shelf_label)
print(copy_1.title == copy_2.title)

print(copy_1.check_out())
print(copy_1.check_out())
print(copy_1.available, copy_2.available, shelf_label.available)

copy_1.check_in()
print(copy_1.available)
