"""Draws the die, the buttons and the bar chart of the counts. All rolling and counting comes from dice.py."""
import kcsgame
import dice

WIDTH, HEIGHT = 420, 390
INK = "#172440"
MUTED = "#657186"
BAR = "#0d397a"
DIE = "#b5452f"
PIPS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)],
        4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
        6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}
BUTTONS = {"roll": (150, 18, 250, 34, "Roll the die"),
           "one": (150, 60, 250, 34, "Simulate 1,000 rolls"),
           "two": (150, 102, 250, 34, "Simulate two dice")}
TOTAL = 1000
STEP = 10


def main():
    win = kcsgame.Window(WIDTH, HEIGHT)
    two_dice = dice.count_totals(1) is not None
    state = {"face": 1, "spin": 0, "mode": "one", "counts": {}, "left": 0}

    def button(key):
        x, y, w, h, label = BUTTONS[key]
        win.rect(x, y, w, h, "#f5f8fb")
        win.rect(x, y, w, h, BAR, fill=False)
        win.text(x + w / 2, y + h / 2, label, size=15, color=BAR, align="center")

    def die(face):
        win.rect(20, 18, 110, 110, DIE)
        for dx, dy in PIPS.get(face, []):
            win.circle(75 + dx * 30, 73 + dy * 30, 9, "#ffffff")
        if face not in PIPS:
            win.text(75, 73, str(face), size=30, color="#ffffff", align="center")

    def chart():
        counts = state["counts"]
        faces = sorted(counts)
        if not faces:
            win.text(WIDTH / 2, 270, "Simulate rolls to see how often each result appears.", size=14, color=MUTED, align="center")
            return
        top = max(max(counts.values()), 1)
        width = (WIDTH - 40) / len(faces)
        for i, face in enumerate(faces):
            height = 170 * counts[face] / top
            x = 20 + i * width
            win.rect(x + 3, 345 - height, width - 6, height, BAR)
            win.text(x + width / 2, 360, face, size=14, color=INK, align="center")
            win.text(x + width / 2, 335 - height, counts[face], size=11, color=MUTED, align="center")
        win.line(15, 345, WIDTH - 15, 345, INK, width=2)

    def draw():
        win.clear("#ffffff")
        die(state["face"])
        button("roll")
        button("one")
        if two_dice:
            button("two")
        chart()

    def add(counts):
        for key, number in counts.items():
            state["counts"][key] = state["counts"].get(key, 0) + number

    def report():
        rolls = sum(state["counts"].values())
        if state["mode"] == "one":
            mean = dice.average(state["counts"])
            win.status(f"{rolls:,} rolls: average {mean:.2f} (a fair die averages 3.5)")
        else:
            common = max(state["counts"], key=state["counts"].get)
            win.status(f"{rolls:,} rolls of two dice: the most common total so far is {common}")

    def frame(seconds):
        if state["spin"] > 0:
            state["spin"] -= 1
            state["face"] = dice.roll()
            if state["spin"] == 0:
                win.status(f"You rolled a {state['face']}.")
            draw()
        if state["left"] > 0:
            step = min(STEP, state["left"])
            add(dice.count_rolls(step) if state["mode"] == "one" else dice.count_totals(step))
            state["left"] -= step
            report()
            draw()

    def inside(key, x, y):
        bx, by, bw, bh, label = BUTTONS[key]
        return bx <= x <= bx + bw and by <= y <= by + bh

    def click(x, y):
        if inside("roll", x, y):
            state["spin"] = 12
        elif inside("one", x, y):
            state.update(mode="one", counts={}, left=TOTAL)
        elif two_dice and inside("two", x, y):
            state.update(mode="two", counts={}, left=TOTAL)

    win.on_click(click)
    win.every_frame(frame)
    win.status("Roll the die, or simulate 1,000 rolls.")
    draw()
