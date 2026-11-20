"""Controller: turns desk commands into calls on the model and results for the view."""

HELP = "Commands: list, borrow <copy> <member>, return <copy>, overdue, help, quit"


class DeskController:
    def __init__(self, library, view, today):
        self.library = library
        self.view = view
        self.today = today

    def handle(self, command_line):
        words = command_line.split()
        if not words:
            return True
        command, arguments = words[0], words[1:]
        try:
            if command == "quit":
                return False
            elif command == "list":
                self.view.show_lines(self.library.catalogue.report())
            elif command == "borrow" and len(arguments) == 2:
                loan = self.library.lend(arguments[0], arguments[1], self.today)
                self.view.show_message(f"Lent {loan.book.title} to {loan.member.name}")
            elif command == "return" and len(arguments) == 1:
                loan = self.library.return_book(arguments[0], self.today)
                self.view.show_message(f"Returned {loan.book.title}")
            elif command == "overdue":
                lines = [f"{loan.book.title}: {loan.member.name}" for loan in self.library.overdue_loans(self.today)]
                self.view.show_lines(lines or ["No overdue loans"])
            else:
                self.view.show_message(HELP)
        except ValueError as error:
            self.view.show_message(f"Refused: {error}")
        return True

    def run(self):
        self.view.show_message(HELP)
        while self.handle(self.view.ask_command()):
            pass
