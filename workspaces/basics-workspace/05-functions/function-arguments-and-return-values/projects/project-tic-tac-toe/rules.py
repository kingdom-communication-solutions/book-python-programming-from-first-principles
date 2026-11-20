"""Tic-Tac-Toe rules.

The board is a list of three rows. Each row is a list of three cells, and each cell holds
"X", "O" or "" (empty). board[row][col] is the cell in that row and column, counted from 0.
"""


def new_board():
    """Return an empty board."""
    return [["", "", ""], ["", "", ""], ["", "", ""]]


def place(board, row, col, player):
    """Put the player's mark in an empty cell and return True; return False if the cell is taken."""
    if board[row][col] != "":
        return False
    board[row][col] = player
    return True


# Task 1 - Complete
# Return True when no empty cell is left, otherwise False.
def is_full(board):
    # TODO: visit every cell with two nested for loops and return False at the first empty cell.
    return False


# Task 2 - Correct the AI code
# An assistant might answer the request "Write winner(board) for Tic-Tac-Toe" like this.
# Predict what happens when X fills a diagonal, play to check, then find and fix the mistake.
def winner(board):
    """Return "X" or "O" if that player has three in a row, otherwise ""."""
    for row in board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    return ""


# Task 3 - Extend (optional)
# Return the computer's move as (row, col): the centre if it is free, otherwise the first free cell.
# While this function returns None, two people play against each other.
def computer_move(board):
    # TODO: your rule for the computer player
    return None
