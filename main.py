from time import sleep
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
    main()
