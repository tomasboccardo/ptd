from time import sleep
from ptd.view.drawer import ConsoleViewDrawer


class PtdInteractiveApp(object):
    def __enter__(self):
        self.window = ConsoleViewDrawer()
        return self

    def loop(self):
        self.window.print_line("Hello World!", 0)
        self.window.print_line("olleH", 2)
        sleep(5)

    def __exit__(self, type, value, traceback):
        del self.window
