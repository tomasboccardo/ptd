import pytest

from ptd.service.command.add import PtdAddCommand
from ptd.service.command.factory import PtdCommandFactory
from ptd.util.exceptions import PtdCommandNotFoundException


def test_command_factory_for_add_command():
    command = PtdCommandFactory.get_command('add')
    assert isinstance(command, PtdAddCommand)


def test_command_factory_for_non_existing_command_raises_exception():
    with pytest.raises(PtdCommandNotFoundException):
        command = PtdCommandFactory.get_command('non-existing')
