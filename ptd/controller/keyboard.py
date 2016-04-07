import logging
import curses


logger = logging.getLogger('ptd')


class KeyboardController(object):
    def __init__(self):
        self.handlers = {}

    def handler(self, event):
        def decorator(fn):
            self.handlers[event] = fn
            return fn
        return decorator

    def trigger_event(self, event, input_ev):
        handler = self.handlers.get(event)
        if handler is not None and callable(handler):
            handler(input_ev)

    def handle_input(self, input_event):
        logger.debug('Pressed: {}'.format(input_event))
        self.trigger_event(input_event, input_event)
