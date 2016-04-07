import logging

from ptd import config
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
        @controller.handler(config.exit_key)
        def exit_handler():
            logger.info('Exit sequence started')
            self.looping = False

        @controller.handler(config.power_key)
        def power_handler():
            self.window.enable_power_mode()

        @controller.handler(config.resize_event)
        def resize_handler():
            self.window.on_resize()

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
