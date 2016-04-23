from ptd.model.todo import PtdTodoList


def test_todo_list_creation_default():
    todo_list = PtdTodoList('List Name')

    assert todo_list.name == 'List Name'
    assert len(todo_list.tasks) == 0
