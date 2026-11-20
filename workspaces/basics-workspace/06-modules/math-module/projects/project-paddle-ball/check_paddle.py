"""Checks for the Paddle Ball tasks. Run them with:  python check_paddle.py"""
import paddle


def ball(x=100, y=100, angle=0, speed=100):
    return {"x": x, "y": y, "angle": angle, "speed": speed}


def bounced(b, height=320):
    paddle.bounce_wall(b, height)
    return b


def moved(b, seconds=1):
    paddle.move(b, seconds)
    return round(b["x"], 1), round(b["y"], 1)


def faster(speed):
    b = ball(speed=speed)
    paddle.speed_up(b)
    return round(b["speed"], 1)


CHECKS = [
    ("Task 1: a ball above the top wall turns down", lambda: bounced(ball(y=2, angle=30))["angle"] == -30),
    ("Task 1: it is put back at the top wall", lambda: bounced(ball(y=2, angle=30))["y"] == paddle.RADIUS),
    ("Task 1: a ball below the bottom wall turns up", lambda: bounced(ball(y=330, angle=-45))["angle"] == 45),
    ("Task 1: it is put back at the bottom wall", lambda: bounced(ball(y=330, angle=-45))["y"] == 320 - paddle.RADIUS),
    ("Task 1: a ball in the middle keeps its angle", lambda: bounced(ball(y=160, angle=30))["angle"] == 30),
    ("Task 2: angle 0 moves the ball to the right", lambda: moved(ball(angle=0)) == (200.0, 100.0)),
    ("Task 2: angle 90 moves the ball straight up", lambda: moved(ball(angle=90)) == (100.0, 0.0)),
    ("Task 2: angle 180 moves the ball to the left", lambda: moved(ball(angle=180)) == (0.0, 100.0)),
    ("Task 2: angle -30 moves right and down", lambda: moved(ball(angle=-30)) == (186.6, 150.0)),
]

OPTIONAL = [
    ("Task 3: a hit makes the ball 10 percent faster", lambda: faster(300) == 330.0),
    ("Task 3: the speed never exceeds 600", lambda: faster(590) == 600),
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
    if faster(300) != 300:
        print()
        extra = run(OPTIONAL)
        print(f"{extra} of {len(OPTIONAL)} optional checks passed.")
