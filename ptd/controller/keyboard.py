import logging
from ptd import config

logger = logging.getLogger('ptd')


class KeyboardController(object):
    def __init__(self):
        self.handlers = {}

    def handler(self, event=None):
        def decorator(fn):
            if event is None or event == 'default':
                self.handlers['default'] = fn
            else:
                ev = ord(event) if isinstance(event, str) else event
                self.handlers[ev] = fn
            return fn
        return decorator

    def setup_input(self, input_line):
        @self.handler()
        def write_handler(value):
            input_line.write_char(chr(value))

        @self.handler(config.backspace_key)
        def backspace_handler(value):
            input_line.remove_last()

    def trigger_event(self, event, input_ev):
        handler = self.handlers.get(event)
        if handler is not None and callable(handler):
            handler(input_ev)
        else:
            self.handlers.get('default')(input_ev)

    def handle_input(self, input_event):
        logger.debug('Pressed: {}'.format(input_event))
        self.trigger_event(input_event, input_event)
