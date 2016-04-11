import argparse
import logging
import traceback

from ptd_lib import config
from ptd_lib.app import PtdApp
from ptd_lib.config import strings
from ptd_lib.interactive_app import PtdInteractiveApp


logging.basicConfig(filename='ptd.log')
logger = logging.getLogger('ptd')
logger.setLevel(logging.DEBUG)


def parse_args():
    parser = argparse.ArgumentParser(prog='ptd', description=strings.args_parser_descrption)
    parser.add_argument('command', default='help', help=strings.args_command_help_text)
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(config.version))

    args = parser.parse_args()
    if args.command == 'help':
        parser.print_help()
        exit(1)

    return args


def start_gui():
    with PtdInteractiveApp() as app:
        logger.info('Starting app loop')
        app.loop()
        logger.info('Exiting')


def run_command(args):
    app = PtdApp()
    app.run_command(args.command)


def main():
    args = parse_args()

    if args.command == 'gui':
        start_gui()
    else:
        run_command(args)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(traceback.format_exc())
        logger.error(str(e))
        raise e
