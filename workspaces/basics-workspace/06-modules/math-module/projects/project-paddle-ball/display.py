"""Draws the court and handles the keys. The ball's movement and bounces all come from paddle.py."""
import kcsgame
import paddle

WIDTH, HEIGHT = 480, 320
PADDLE_W, PADDLE_H = 10, 64
LEFT_X, RIGHT_X = 24, WIDTH - 24 - PADDLE_W
PADDLE_SPEED = 300
INK = "#172440"
BALL = "#b5452f"


def main():
    win = kcsgame.Window(WIDTH, HEIGHT)
    game = {"left": HEIGHT / 2, "right": HEIGHT / 2, "score": [0, 0],
            "ball": paddle.new_ball(WIDTH, HEIGHT), "playing": False}

    def draw():
        win.clear("#ffffff")
        for y in range(0, HEIGHT, 24):
            win.line(WIDTH / 2, y + 4, WIDTH / 2, y + 14, "#c7d0dc", width=2)
        win.text(WIDTH / 2 - 40, 24, game["score"][0], size=26, color=INK, align="center")
        win.text(WIDTH / 2 + 40, 24, game["score"][1], size=26, color=INK, align="center")
        win.rect(LEFT_X, game["left"] - PADDLE_H / 2, PADDLE_W, PADDLE_H, INK)
        win.rect(RIGHT_X, game["right"] - PADDLE_H / 2, PADDLE_W, PADDLE_H, INK)
        ball = game["ball"]
        win.circle(ball["x"], ball["y"], paddle.RADIUS, BALL)
        if not game["playing"]:
            win.text(WIDTH / 2, HEIGHT - 30, "Click the court, then press the space bar", size=15, color="#657186", align="center")

    def steer(side, up, down, seconds):
        if win.key_down(up):
            game[side] -= PADDLE_SPEED * seconds
        if win.key_down(down):
            game[side] += PADDLE_SPEED * seconds
        game[side] = min(max(game[side], PADDLE_H / 2), HEIGHT - PADDLE_H / 2)

    def hits(side, x):
        ball = game["ball"]
        return abs(ball["y"] - game[side]) <= PADDLE_H / 2 + paddle.RADIUS and abs(ball["x"] - x) <= paddle.RADIUS + PADDLE_W / 2

    def frame(seconds):
        if not game["playing"]:
            return
        steer("left", "w", "s", seconds)
        steer("right", "ArrowUp", "ArrowDown", seconds)
        ball = game["ball"]
        paddle.move(ball, seconds)
        paddle.bounce_wall(ball, HEIGHT)
        if hits("left", LEFT_X + PADDLE_W / 2) and ball["x"] > LEFT_X:
            paddle.bounce_paddle(ball, LEFT_X + PADDLE_W + paddle.RADIUS)
            paddle.speed_up(ball)
        elif hits("right", RIGHT_X + PADDLE_W / 2) and ball["x"] < RIGHT_X + PADDLE_W:
            paddle.bounce_paddle(ball, RIGHT_X - paddle.RADIUS)
            paddle.speed_up(ball)
        if ball["x"] < 0 or ball["x"] > WIDTH or ball["y"] < -40 or ball["y"] > HEIGHT + 40:
            if ball["x"] < WIDTH / 2:
                game["score"][1] += 1
            else:
                game["score"][0] += 1
            game["ball"] = paddle.new_ball(WIDTH, HEIGHT, to_right=ball["x"] < WIDTH / 2)
            game["playing"] = False
            win.status(f"Left {game['score'][0]} : {game['score'][1]} Right. Press the space bar to serve.")
        draw()

    def key(name):
        if name == " " and not game["playing"]:
            game["playing"] = True
            win.status("Left player: W and S. Right player: ↑ and ↓.")

    win.on_key(key)
    win.every_frame(frame)
    win.status("Click the court, then press the space bar to serve.")
    draw()
