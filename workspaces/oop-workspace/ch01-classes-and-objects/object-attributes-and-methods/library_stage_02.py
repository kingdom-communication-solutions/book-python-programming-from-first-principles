"""Library stage 02: attributes on Book objects and a description() method."""


class Book:
    def description(self):
        return f"{self.title} by {self.author} ({self.year})"


river = Book()
river.title = "River Stories"
river.author = "A. Mensah"
river.year = 2024

maps = Book()
maps.title = "Silent Maps"
maps.author = "L. Chen"
maps.year = 2021

print(river.description())
print(maps.description())
