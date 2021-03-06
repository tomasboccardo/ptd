import pytest

from ptd.service.command.add import PtdAddCommand
from ptd.service.command.factory import PtdCommandFactory
from ptd.util.exceptions import PtdCommandNotFoundException, \
    PtdNoNameSpecifiedException, PtdTodoListNotFoundException


def test_command_factory_for_add_command(ptd_app):
    command = PtdCommandFactory.get_command(ptd_app, 'add')
    assert isinstance(command, PtdAddCommand)


def test_command_factory_for_non_existing_command_raises_exception(ptd_app):
    with pytest.raises(PtdCommandNotFoundException):
        command = PtdCommandFactory.get_command(ptd_app, 'non-existing')


def test_add_command_creates_new_task_on_default_todo_list(ptd_app):
    command = PtdAddCommand(ptd_app)
    assert len(ptd_app.get_todo_list('default').tasks) == 0

    command.execute(
        name='New Task',
        description='Newly created task',
        priority=5,
    )

    assert len(ptd_app.get_todo_list('default').tasks) == 1
    assert ptd_app.get_todo_list('default').tasks[0].name == 'New Task'


def test_add_command_creates_new_task_without_description_and_priority(ptd_app):
    command = PtdAddCommand(ptd_app)
    assert len(ptd_app.get_todo_list('default').tasks) == 0

    command.execute(
        name='New Task'
    )

    assert len(ptd_app.get_todo_list('default').tasks) == 1
    assert ptd_app.get_todo_list('default').tasks[0].name == 'New Task'


def test_add_command_creates_new_task_without_name_raises_exception(ptd_app):
    command = PtdAddCommand(ptd_app)
    assert len(ptd_app.get_todo_list('default').tasks) == 0

    with pytest.raises(PtdNoNameSpecifiedException):
        command.execute(
            description='Newly created task',
            priority=5,
        )

def test_add_command_creates_new_task_on_non_existing_todo_list_raises_exception(ptd_app):
    command = PtdAddCommand(ptd_app)

    with pytest.raises(PtdTodoListNotFoundException):
        command.execute(
            name='New Task',
            todo_list_name='non-default'
        )
