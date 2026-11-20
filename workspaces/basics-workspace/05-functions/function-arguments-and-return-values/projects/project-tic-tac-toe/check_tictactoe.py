"""Checks for the Tic-Tac-Toe tasks. Run them with:  python check_tictactoe.py"""
import rules


def board(text):
    """Build a board from three strings such as "XO.", where "." is an empty cell."""
    return [["" if c == "." else c for c in line] for line in text.split()]


CHECKS = [
    ("Task 1: an empty board is not full", lambda: rules.is_full(rules.new_board()) is False),
    ("Task 1: a board with one empty cell is not full", lambda: rules.is_full(board("XOX OXO OX.")) is False),
    ("Task 1: a board without empty cells is full", lambda: rules.is_full(board("XOX OXO OXO")) is True),
    ("Task 2: three in a row wins", lambda: rules.winner(board("XXX OO. ...")) == "X"),
    ("Task 2: three in a column wins", lambda: rules.winner(board("OX. OX. O..")) == "O"),
    ("Task 2: the diagonal from top left wins", lambda: rules.winner(board("X.O .XO ..X")) == "X"),
    ("Task 2: the diagonal from top right wins", lambda: rules.winner(board("XXO .O. OX.")) == "O"),
    ("Task 2: no winner on a mixed board", lambda: rules.winner(board("XOX OXO OXO")) == ""),
]

OPTIONAL = [
    ("Task 3: the computer takes the free centre", lambda: rules.computer_move(board("X.. ... ...")) == (1, 1)),
    ("Task 3: otherwise the first free cell", lambda: rules.computer_move(board("X.. .O. ...")) == (0, 1)),
]


def run(checks):
    passed = 0
    for name, test in checks:
        try:
            ok = test()
        except Exception as error:  # a crash in the learner's code counts as a failed check
            ok = False
            name += f"  ({type(error).__name__}: {error})"
        print(("✓ " if ok else "✗ ") + name)
        passed += ok
    return passed


if __name__ == "__main__":
    passed = run(CHECKS)
    print(f"{passed} of {len(CHECKS)} checks passed.")
    if rules.computer_move(rules.new_board()) is not None:
        print()
        extra = run(OPTIONAL)
        print(f"{extra} of {len(OPTIONAL)} optional checks passed.")
