"""Draws the Tic-Tac-Toe board and handles clicks. The game's decisions all come from rules.py."""
import kcsgame
import rules

CELL = 110
SIZE = 3 * CELL
INK = "#172440"
X_COLOR = "#0d397a"
O_COLOR = "#b5452f"


def main():
    win = kcsgame.Window(SIZE, SIZE)
    game = {"board": rules.new_board(), "player": "X", "over": False}

    def draw():
        win.clear("#ffffff")
        for i in (1, 2):
            win.line(i * CELL, 10, i * CELL, SIZE - 10, INK, width=4)
            win.line(10, i * CELL, SIZE - 10, i * CELL, INK, width=4)
        for row in range(3):
            for col in range(3):
                x, y = col * CELL + CELL // 2, row * CELL + CELL // 2
                mark = game["board"][row][col]
                if mark == "X":
                    win.line(x - 30, y - 30, x + 30, y + 30, X_COLOR, width=9)
                    win.line(x + 30, y - 30, x - 30, y + 30, X_COLOR, width=9)
                elif mark == "O":
                    win.circle(x, y, 33, O_COLOR, fill=False, line_width=9)

    def finish_turn():
        won = rules.winner(game["board"])
        if won:
            game["over"] = True
            win.status(f"{won} wins! Click the board to play again.")
        elif rules.is_full(game["board"]):
            game["over"] = True
            win.status("A draw. Click the board to play again.")
        else:
            game["player"] = "O" if game["player"] == "X" else "X"
            win.status(f"{game['player']} to play")

    def click(x, y):
        if game["over"]:
            game.update(board=rules.new_board(), player="X", over=False)
            win.status("X to play")
            draw()
            return
        row, col = int(y // CELL), int(x // CELL)
        if not (0 <= row < 3 and 0 <= col < 3) or not rules.place(game["board"], row, col, game["player"]):
            return
        finish_turn()
        if not game["over"] and game["player"] == "O":
            move = rules.computer_move(game["board"])
            if move is not None:
                if not rules.place(game["board"], move[0], move[1], "O"):
                    raise ValueError(f"computer_move returned {move}, but that cell is not free")
                finish_turn()
        draw()

    win.on_click(click)
    win.status("X to play")
    draw()
