import pytest

from ptd.service.command.add import PtdAddCommand
from ptd.service.command.factory import PtdCommandFactory
from ptd.util.exceptions import PtdCommandNotFoundException


def test_command_factory_for_add_command(ptd_app):
    command = PtdCommandFactory.get_command(ptd_app, 'add')
    assert isinstance(command, PtdAddCommand)


def test_command_factory_for_non_existing_command_raises_exception(ptd_app):
    with pytest.raises(PtdCommandNotFoundException):
        command = PtdCommandFactory.get_command(ptd_app, 'non-existing')
