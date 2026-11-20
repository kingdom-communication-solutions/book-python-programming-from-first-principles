"""Library stage 03: __init__ gives every Book its starting attributes."""


class Book:
    def __init__(self, copy_id, title, author, year):
        self.copy_id = copy_id
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"{self.title} by {self.author} ({self.year})"


river = Book("B001", "River Stories", "A. Mensah", 2024)
maps = Book("B002", "Silent Maps", "L. Chen", 2021)

print(river.copy_id, river.description())
print(maps.copy_id, maps.description())
