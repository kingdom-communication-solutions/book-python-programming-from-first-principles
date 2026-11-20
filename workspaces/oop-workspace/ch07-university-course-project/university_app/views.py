"""Console view for the University Course System. Complete; no changes needed."""


class ConsoleView:
    def ask_command(self):
        return input("office> ")

    def show_lines(self, lines):
        for line in lines:
            print(line)

    def show_message(self, message):
        print(message)
