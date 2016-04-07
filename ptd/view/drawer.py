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

    def refresh(self):
        self.stdscr.refresh()

    def __del__(self):
        # Revert all initialized configurations
        curses.echo()
        curses.nocbreak()
        self.stdscr.keypad(0)
        # End curses app
        curses.endwin()
