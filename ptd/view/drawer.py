import logging
import curses

logger = logging.getLogger('ptd')


class ConsoleViewDrawer(object):
    def __init__(self):
        # Initialize curses library
        self.stdscr = curses.initscr()
        # Disable automatic echoing of pressed keys
        curses.noecho()
        curses.curs_set(0)
        # React instalty when a key is pressed (do not wait for Enter Key)
        curses.cbreak()
        # Ask curses to handle special keys
        self.stdscr.keypad(1)
        self.power_mode = False
        self.height = 0
        self.width = 0
        self.set_size()

    def read_input(self):
        return self.stdscr.getch()

    def clear_line(self, line):
        self.stdscr.move(line, 0)
        self.stdscr.clrtoeol()

    def print_line(self, text, line):
        self.stdscr.addstr(line, 0, text)

    def set_size(self):
        self.height, self.width = self.stdscr.getmaxyx()
        # logger.debug('Window size {}x{}'.format(self.width, self.height))
        self.stdscr.hline(self.height - 2, 0, '_', self.width)

    def on_resize(self):
        prev_height = self.height
        self.set_size()
        if self.height > prev_height:
            self.clear_line(prev_height - 2)

        self.refresh()

    def refresh(self):
        self.stdscr.refresh()

    def write_char(self, char):
        if not self.power_mode:
            return
        y, x = self.stdscr.getyx()
        max_y, max_x = self.stdscr.getmaxyx()
        if x >= max_x:
            return
        self.stdscr.addch(y, x, char)
        self.stdscr.addch(y, x + 1, '_', curses.A_BLINK)
        self.stdscr.move(y, x + 1)

    def remove_last(self):
        if not self.power_mode:
            return
        y, x = self.stdscr.getyx()
        if x - 1 < 0:
            return
        self.stdscr.addch(y, x, ' ')
        self.stdscr.addch(y, x - 1, '_', curses.A_BLINK)
        self.stdscr.move(y, x - 1)

    def enable_power_mode(self):
        self.power_mode = True
        self.stdscr.addch(self.height - 1, 0, ':')
        self.stdscr.addch(self.height - 1, 1, '_', curses.A_BLINK)
        self.stdscr.move(self.height - 1, 1)
        self.refresh()

    def disable_power_mode(self):
        self.power_mode = False
        self.clear_line(self.height - 1)

    def __del__(self):
        # Revert all initialized configurations
        curses.echo()
        curses.nocbreak()
        self.stdscr.keypad(0)
        # End curses app
        curses.endwin()
