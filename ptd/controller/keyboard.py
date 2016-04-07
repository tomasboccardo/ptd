import logging

logger = logging.getLogger('ptd')


class KeyboardController(object):
    def __init__(self):
        self.handlers = {}

    def handler(self, event):
        def decorator(fn):
            ev = ord(event) if isinstance(event, basestring) else event
            self.handlers[ev] = fn
            return fn
        return decorator

    def trigger_event(self, event, input_ev):
        handler = self.handlers.get(event)
        if handler is not None and callable(handler):
            handler()

    def handle_input(self, input_event):
        logger.debug('Pressed: {}'.format(input_event))
        self.trigger_event(input_event, input_event)
