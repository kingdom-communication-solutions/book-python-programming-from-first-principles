from collections import Counter, defaultdict, namedtuple, deque

Book = namedtuple("Book", ["copy_id", "title", "category"])
books = [
    Book("B1", "River Stories", "History"),
    Book("B2", "Silent Maps", "Science"),
    Book("B3", "City Letters", "History"),
]
requests = deque(["B3", "B1"])

# TODO: count books by category and group titles, preserving their order.
# TODO: index books by copy ID, then serve requests from the left.
# TODO: print the counts, groups and requested titles shown in the book.
