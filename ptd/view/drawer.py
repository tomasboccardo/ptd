import logging
import curses


logger = logging.getLogger('ptd')


class ConsoleViewDrawer(object):
    def __init__(self):
        # Initialize curses library
        self.stdscr = curses.initscr()
        # Disable automatic echoing of pressed keys
        curses.noecho()
        # React instalty when a key is pressed (do not wait for Enter Key)
        curses.cbreak()
        # Ask curses to handle special keys
        self.stdscr.keypad(1)
        self._on_resize()

    def print_line(self, text, line):
        self.stdscr.move(line, 0)
        self.stdscr.clrtoeol()
        self.stdscr.addstr(line, 0, text)
        self.stdscr.refresh()

    def _on_resize(self):
        self.height, self.width = self.stdscr.getmaxyx()
        logger.debug('Window size {}x{}'.format(self.width, self.height))
        self.stdscr.hline(self.height - 2, 0, '_', self.width - 1)
        self.stdscr.refresh()

    def __del__(self):
        # Revert all initialized configurations
        curses.echo()
        curses.nocbreak()
        self.stdscr.keypad(0)
        # End curses app
        curses.endwin()
