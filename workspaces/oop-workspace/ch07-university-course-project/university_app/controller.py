"""Controller for the University Course System.

Starter file. The command "courses" is implemented as an example; add the
other commands in Milestone 5.
"""

HELP = "Commands: courses, help, quit"


class OfficeController:
    def __init__(self, university, view):
        self.university = university
        self.view = view

    def handle(self, command_line):
        words = command_line.split()
        if not words:
            return True
        command, args = words[0], words[1:]
        try:
            if command == "quit":
                return False
            elif command == "courses":
                self.view.show_lines(self.university.courses())
            # TODO: enroll, grade, transcript and students
            else:
                self.view.show_message(HELP)
        except ValueError as error:
            self.view.show_message(f"Refused: {error}")
        return True

    def run(self):
        self.view.show_message(HELP)
        while self.handle(self.view.ask_command()):
            pass
