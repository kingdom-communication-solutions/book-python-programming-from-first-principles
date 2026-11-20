"""Library stage 15: a logging mixin combined with a notifier through multiple inheritance."""
from abc import ABC, abstractmethod
from datetime import date, timedelta

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


class EBook(Book):
    loan_days = 21

    def __init__(self, copy_id, title, author, year, file_format):
        super().__init__(copy_id, title, author, year)
        self.file_format = file_format

    def description(self):
        return super().description() + f" [{self.file_format}]"


class ReferenceBook(Book):
    loan_days = 0

    def check_out(self):
        raise ValueError(f"{self.copy_id} is for reference only")


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

    def report(self):
        return [f"{book.copy_id} {book.description()}" for book in self._books.values()]


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Loan:
    def __init__(self, book, member, start, due):
        self.book = book
        self.member = member
        self.start = start
        self.due = due
        self.returned = None

    @property
    def active(self):
        return self.returned is None

    def days_late(self, on_date):
        return max(0, (on_date - self.due).days)


class Notifier(ABC):
    @abstractmethod
    def send(self, member, message):
        """Deliver one message to a member."""

    def send_many(self, members, message):
        for member in members:
            self.send(member, message)


class ConsoleNotifier(Notifier):
    def send(self, member, message):
        print(f"To {member.name}: {message}")


class MemoryNotifier(Notifier):
    def __init__(self):
        self.messages = []

    def send(self, member, message):
        self.messages.append((member.member_id, message))


class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = []

    def send(self, member, message):
        self.log.append(f"{member.member_id}: {message}")
        super().send(member, message)


class LoggingConsoleNotifier(LogMixin, ConsoleNotifier):
    pass


class Library:
    def __init__(self, name, notifier):
        self.name = name
        self.catalogue = Catalogue()
        self._members = {}
        self._loans = []
        self.notifier = notifier

    def add_member(self, member):
        if member.member_id in self._members:
            raise ValueError(f"Duplicate member ID: {member.member_id}")
        self._members[member.member_id] = member

    def lend(self, copy_id, member_id, today):
        book = self.catalogue.find(copy_id)
        member = self._members.get(member_id)
        if book is None or member is None:
            raise ValueError("Unknown book or member")
        book.check_out()
        loan = Loan(book, member, today, today + timedelta(days=book.loan_days))
        self._loans.append(loan)
        self.notifier.send(member, f"{book.title} is due on {loan.due}")
        return loan

    def return_book(self, copy_id, today):
        for loan in self._loans:
            if loan.active and loan.book.copy_id == copy_id:
                loan.book.check_in()
                loan.returned = today
                late = loan.days_late(today)
                if late:
                    self.notifier.send(loan.member, f"{loan.book.title} was returned {late} days late")
                return loan
        raise ValueError(f"{copy_id} has no active loan")

    def active_titles(self, member_id):
        return [loan.book.title for loan in self._loans
                if loan.active and loan.member.member_id == member_id]


def build_library(notifier):
    library = Library("Central", notifier)
    for record in [
        "B001;River Stories;A. Mensah;2024",
        "B002;Silent Maps;L. Chen;2021",
    ]:
        library.catalogue.add(Book.from_record(record))
    library.catalogue.add(EBook("B003", "City Letters", "K. Owusu", 2019, "EPUB"))
    library.catalogue.add(ReferenceBook("B004", "Atlas of Ghana", "Survey Office", 2015))
    library.add_member(Member("M001", "Ada"))
    library.add_member(Member("M002", "Kofi"))
    return library


if __name__ == "__main__":
    notifier = LoggingConsoleNotifier()
    library = build_library(notifier)
    library.lend("B001", "M001", date(2026, 3, 2))
    library.return_book("B001", date(2026, 3, 20))
    print(notifier.log)
    print([cls.__name__ for cls in LoggingConsoleNotifier.__mro__])
