import logging

from ptd_lib import config
from ptd_lib.view.drawer import ConsoleViewDrawer
from ptd_lib.controller.keyboard import KeyboardController
from ptd_lib.view.input_line import InputTextLine

logger = logging.getLogger('ptd')


class PtdInteractiveApp(object):
    def __init__(self):
        self.looping = True
        self.power_mode = False

    def __enter__(self):
        self.window = ConsoleViewDrawer()
        self.input_line = InputTextLine(self.window, self.window.height - 1, 0, ':', '_')
        self.controller = KeyboardController()
        self._setup_handlers(self.controller)
        return self

    def _setup_handlers(self, controller):
        @controller.handler(config.exit_key)
        def exit_handler(value):
            self._exit()

        @controller.handler(config.power_key)
        def power_handler(value):
            self.activate_power_mode()

        @controller.handler(config.esc_key)
        @controller.handler(config.enter_key)
        def enter_handler(value):
            if value == config.enter_key:
                logger.debug('You press enter')
            self.deactivate_power_mode()

        @controller.handler(config.resize_event)
        def resize_handler(value):
            self.window.on_resize()
            self.input_line.on_resize()
            self.window.refresh()

    def activate_power_mode(self):
        if self.power_mode:
            return
        self.power_mode = True
        self.controller.setup_input(self.input_line)

    def deactivate_power_mode(self):
        if not self.power_mode:
            return
        self.power_mode = False
        self.input_line.erase()

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
