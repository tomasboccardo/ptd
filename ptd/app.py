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
        def exit_handler(value):
            self._exit()

        @controller.handler(config.power_key)
        def power_handler(value):
            self.window.enable_power_mode()

        @controller.handler(config.esc_key)
        @controller.handler(config.enter_key)
        def enter_handler(value):
            if value == config.enter_key:
                logger.debug('You press enter')
            self.window.disable_power_mode()

        @controller.handler(config.resize_event)
        def resize_handler(value):
            self.window.on_resize()

        @controller.handler(config.backspace_key)
        def write_handler(value):
            self.window.remove_last()

        @controller.handler()
        def write_handler(value):
            self.window.write_char(chr(value))

    def _get_input(self):
        return self.window.read_input()

    def _loop(self):
        input_event = self._get_input()
        self.controller.handle_input(input_event)

    def loop(self):
        while self.looping:
            self._loop()
            self.window.refresh()

    def _exit(self):
        logger.info('Exit sequence started')
        self.looping = False

    def __exit__(self, type, value, traceback):
        del self.window
