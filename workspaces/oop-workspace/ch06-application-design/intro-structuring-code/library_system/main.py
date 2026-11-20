"""Start the Library system: create objects from the two modules and use them."""
from datetime import date

from library_model import Book, EBook, ReferenceBook, Member, Library
from notifications import ConsoleNotifier


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


def main():
    library = build_library(ConsoleNotifier())
    library.lend("B001", "M001", date(2026, 3, 2))
    library.return_book("B001", date(2026, 3, 20))
    for line in library.catalogue.report():
        print(line)


if __name__ == "__main__":
    main()
