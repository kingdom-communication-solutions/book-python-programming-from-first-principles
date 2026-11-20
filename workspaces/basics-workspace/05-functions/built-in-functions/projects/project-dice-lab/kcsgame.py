"""kcsgame: a very small drawing library for the book's browser games.

In the online book, a Window draws on the page's canvas. Outside the browser (plain Python) the
same calls do nothing, so a game's rules and checks can still be imported and tested.

    win = Window(360, 410)
    win.clear()
    win.rect(10, 10, 100, 50, "#243f68")
    win.circle(60, 60, 20, "tomato")
    win.line(0, 0, 100, 100, "black", width=3)
    win.text(180, 30, "Hello", size=24, align="center")
    win.on_click(handle_click)        # handle_click(x, y)
    win.on_key(handle_key)            # handle_key(name), e.g. "ArrowUp", "w", " "
    win.every_frame(update)           # update(seconds since the last frame)
    win.key_down("ArrowUp")           # True while the key is held
    win.status("X to play")           # the line of text below the canvas
"""
import traceback

try:
    import js
    from pyodide.ffi import create_proxy
    IN_BROWSER = True
except ImportError:
    IN_BROWSER = False


class Window:
    def __init__(self, width, height, background="#ffffff"):
        self.width = width
        self.height = height
        self.background = background
        self._ctx = None
        if IN_BROWSER:
            js.kcs.reset(width, height)
            self._ctx = js.kcs.context()

    # Drawing -------------------------------------------------------------------------------
    def clear(self, color=None):
        if self._ctx:
            self._ctx.fillStyle = color or self.background
            self._ctx.fillRect(0, 0, self.width, self.height)

    def rect(self, x, y, width, height, color, fill=True, line_width=2):
        if self._ctx:
            if fill:
                self._ctx.fillStyle = color
                self._ctx.fillRect(x, y, width, height)
            else:
                self._ctx.strokeStyle = color
                self._ctx.lineWidth = line_width
                self._ctx.strokeRect(x, y, width, height)

    def circle(self, x, y, radius, color, fill=True, line_width=2):
        if self._ctx:
            self._ctx.beginPath()
            self._ctx.arc(x, y, radius, 0, 6.283185307179586)
            if fill:
                self._ctx.fillStyle = color
                self._ctx.fill()
            else:
                self._ctx.strokeStyle = color
                self._ctx.lineWidth = line_width
                self._ctx.stroke()

    def line(self, x1, y1, x2, y2, color, width=2):
        if self._ctx:
            self._ctx.beginPath()
            self._ctx.moveTo(x1, y1)
            self._ctx.lineTo(x2, y2)
            self._ctx.strokeStyle = color
            self._ctx.lineWidth = width
            self._ctx.lineCap = "round"
            self._ctx.stroke()

    def text(self, x, y, words, size=20, color="#172440", align="left"):
        if self._ctx:
            self._ctx.font = f"600 {size}px system-ui, sans-serif"
            self._ctx.fillStyle = color
            self._ctx.textAlign = align
            self._ctx.textBaseline = "middle"
            self._ctx.fillText(str(words), x, y)

    def status(self, words):
        if IN_BROWSER:
            js.kcs.status(str(words))

    # Events --------------------------------------------------------------------------------
    def on_click(self, handler):
        self._listen("click", handler)

    def on_key(self, handler):
        self._listen("key", handler)

    def every_frame(self, handler):
        self._listen("frame", handler)

    def key_down(self, name):
        return bool(IN_BROWSER and js.kcs.isDown(name))

    def _listen(self, kind, handler):
        if not IN_BROWSER:
            return

        def safe(*args):
            # An error in the learner's code stops the game and is shown below the canvas.
            try:
                handler(*args)
            except Exception:
                js.kcs.fail(traceback.format_exc())

        js.kcs.listen(kind, create_proxy(safe))
