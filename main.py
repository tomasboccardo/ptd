import traceback

import sys

from ptd.app import PtdInteractiveApp
import logging


logging.basicConfig(filename='ptd.log')
logger = logging.getLogger('ptd')
logger.setLevel(logging.DEBUG)


def main():
    with PtdInteractiveApp() as app:
        logger.info('Starting app loop')
        app.loop()
        logger.info('Exiting')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(traceback.format_exc())
        logger.error(str(e))
        raise e
