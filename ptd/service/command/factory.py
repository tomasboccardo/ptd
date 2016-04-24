from ptd.service.command.add import PtdAddCommand
from ptd.util.exceptions import PtdCommandNotFoundException


class PtdCommandFactory(object):

    command_dict = {
        'add': PtdAddCommand
    }

    @staticmethod
    def get_command(command_name):
        command_class = PtdCommandFactory.command_dict.get(command_name)
        if command_class is None:
            raise PtdCommandNotFoundException()
        return command_class()
