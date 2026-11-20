class BookCopy:
    def __init__(self):
        self.available = True

    def borrow(self):
        if not self.available:
            raise ValueError("Already borrowed")
        self.available = False

    def return_book(self):
        if self.available:
            raise ValueError("Already available")
        self.available = True
