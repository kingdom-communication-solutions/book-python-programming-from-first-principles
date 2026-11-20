"""Start the borrowing desk. Optionally pass a date: python main.py 2026-03-02"""
import sys
from datetime import date

from controller import DeskController
from library_model import Book, EBook, ReferenceBook, Member, Library
from notifications import ConsoleNotifier
from views import ConsoleView


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
    today = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    library = build_library(ConsoleNotifier())
    DeskController(library, ConsoleView(), today).run()


if __name__ == "__main__":
    main()
