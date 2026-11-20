"""Paddle Ball rules.

The ball is a dictionary: "x" and "y" give its centre in pixels, measured from the top left corner of the
court (y grows downwards); "angle" is its direction in degrees, measured anticlockwise from "straight
to the right" (90 is straight up); "speed" is in pixels per second.
"""
import math
import random

RADIUS = 8


def new_ball(width, height, to_right=True):
    """Return a ball in the centre of the court, moving to the right or to the left at a random angle."""
    angle = random.choice([-40, -25, 25, 40])
    if not to_right:
        angle = 180 - angle
    return {"x": width / 2, "y": height / 2, "angle": angle, "speed": 260}


def bounce_paddle(ball, x):
    """Reflect the ball from a vertical paddle at position x: the angle becomes 180 minus the angle."""
    ball["x"] = x
    ball["angle"] = (180 - ball["angle"]) % 360


# Task 1 - Complete
# When the ball touches the top wall (y below RADIUS) or the bottom wall (y above height - RADIUS),
# reflect it: put it back at the wall and change its angle to the negative angle.
def bounce_wall(ball, height):
    # TODO: two tests, one for each wall
    pass


# Task 2 - Correct the AI code
# An assistant might answer the request "Write move(ball, seconds): move the ball along its angle" like this.
# Play to see where the ball goes, then find and fix the mistake.
def move(ball, seconds):
    """Move the ball for the given number of seconds along its angle."""
    distance = ball["speed"] * seconds
    ball["x"] += distance * math.cos(ball["angle"])
    ball["y"] -= distance * math.sin(ball["angle"])


# Task 3 - Extend (optional)
# Make the ball 10 percent faster after each paddle hit, but never faster than 600 pixels per second.
def speed_up(ball):
    # TODO
    pass
