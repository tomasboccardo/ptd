import logging
from ptd.view.drawer import ConsoleViewDrawer
from ptd.controller.keyboard import KeyboardController


logger = logging.getLogger('ptd')


class PtdInteractiveApp(object):
    def __enter__(self):
        self.looping = True
        self.window = ConsoleViewDrawer()
        self.controller = KeyboardController()
        self._setup_handlers(self.controller)
        return self

    def _setup_handlers(self, controller):
        @controller.handler(ord('q'))
        def exit_handler(input_event):
            logger.info('Exit sequence started')
            self.looping = False

    def _get_input(self):
        return self.window.read_input()

    def _loop(self):
        self.window.print_line("Hello World!", 0)
        self.window.print_line("olleH", 2)
        input_event = self._get_input()
        self.controller.handle_input(input_event)

    def loop(self):
        while self.looping:
            self._loop()
            self.window.refresh()

    def __exit__(self, type, value, traceback):
        del self.window
