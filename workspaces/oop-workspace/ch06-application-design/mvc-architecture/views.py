"""Console view: everything the borrowing desk shows or asks."""


class ConsoleView:
    def ask_command(self):
        return input("desk> ")

    def show_lines(self, lines):
        for line in lines:
            print(line)

    def show_message(self, message):
        print(message)
