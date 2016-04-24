import pytest

from ptd.model.todo import PtdTodoList, PtdTask
from ptd.util.exceptions import PtdDuplicatedIdException


def test_todo_list_creation_default():
    todo_list = PtdTodoList('List Name')

    assert todo_list.name == 'List Name'
    assert len(todo_list.tasks) == 0


def test_todo_list_adding_task():
    todo_list = PtdTodoList('List Name')
    task = PtdTask(1, 'Test task')

    todo_list.add_task(task)

    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].id == 1
    assert todo_list.tasks[0].name == 'Test task'


def test_todo_list_adding_more_than_one_task():
    todo_list = PtdTodoList('List Name')
    task1 = PtdTask(1, 'Test task 1')
    task2 = PtdTask(2, 'Test task 2')
    task3 = PtdTask(3, 'Test task 3')

    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)

    assert len(todo_list.tasks) == 3
    assert todo_list.tasks[0].id == 1
    assert todo_list.tasks[0].name == 'Test task 1'
    assert todo_list.tasks[1].id == 2
    assert todo_list.tasks[1].name == 'Test task 2'
    assert todo_list.tasks[2].id == 3
    assert todo_list.tasks[2].name == 'Test task 3'


def test_todo_list_adding_more_than_one_task_with_same_id_raises_exception():
    todo_list = PtdTodoList('List Name')
    task1 = PtdTask(1, 'Test task 1')
    task2 = PtdTask(1, 'Test task 2')

    todo_list.add_task(task1)

    with pytest.raises(PtdDuplicatedIdException):
        todo_list.add_task(task2)


def test_todo_list_adding_a_task_with_higher_priority():
    todo_list = PtdTodoList('List Name')
    task1 = PtdTask(1, 'Test task 1', priority=5)
    task2 = PtdTask(2, 'Test task 2', priority=1)

    todo_list.add_task(task1)
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].id == 1
    assert todo_list.tasks[0].name == 'Test task 1'

    todo_list.add_task(task2)
    assert len(todo_list.tasks) == 2
    assert todo_list.tasks[0].id == 2
    assert todo_list.tasks[0].name == 'Test task 2'
    assert todo_list.tasks[1].id == 1
    assert todo_list.tasks[1].name == 'Test task 1'


def test_todo_list_adding_two_tasks_and_modifying_priority_of_one():
    todo_list = PtdTodoList('List Name')
    task1 = PtdTask(1, 'Test task 1')
    task2 = PtdTask(2, 'Test task 2')

    todo_list.add_task(task1)
    todo_list.add_task(task2)

    assert len(todo_list.tasks) == 2
    assert todo_list.tasks[0].id == 1
    assert todo_list.tasks[0].name == 'Test task 1'
    assert todo_list.tasks[1].id == 2
    assert todo_list.tasks[1].name == 'Test task 2'

    task2.priority = 1

    assert len(todo_list.tasks) == 2
    assert todo_list.tasks[0].id == 2
    assert todo_list.tasks[0].name == 'Test task 2'
    assert todo_list.tasks[1].id == 1
    assert todo_list.tasks[1].name == 'Test task 1'
