import curses


class InputTextLine(object):
    def __init__(self, window, y=0, x=0, default='', cursor='_'):
        self.window = window
        self.y = y
        self.x = x
        self.default = default
        self.cursor = cursor

    def write_char(self, char):
        y, x = self.window.stdscr.getyx()
        max_y, max_x = self.window.stdscr.getmaxyx()
        if x >= max_x:
            return
        self.window.stdscr.addch(y, x, char)
        self.window.stdscr.addch(y, x + 1, '_', curses.A_BLINK)
        self.window.stdscr.move(y, x + 1)

    def remove_last(self):
        y, x = self.window.stdscr.getyx()
        if x - 1 < 0:
            return
        self.window.stdscr.addch(y, x, ' ')
        self.window.stdscr.addch(y, x - 1, '_', curses.A_BLINK)
        self.window.stdscr.move(y, x - 1)

    def erase(self):
        self.window.clear_line(self.y)

    def on_resize(self):
        prev_y = self.y
        self.y = self.window.height
        if self.y > prev_y:
            self.window.clear_line(prev_y)