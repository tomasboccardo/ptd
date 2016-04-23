from ptd.model.todo import PtdTask


def test_task_creation_default():
    task = PtdTask(1, 'Test task')

    assert task.id == 1
    assert task.name == 'Test task'
    assert task.description == ''
    assert task.priority == 5
    assert not task.done


def test_task_creation_with_description():
    task = PtdTask(1, 'Test task with description', 'This is an awesome task with description')

    assert task.id == 1
    assert task.name == 'Test task with description'
    assert task.description == 'This is an awesome task with description'
    assert task.priority == 5
    assert not task.done


def test_task_creation_with_description_and_priority():
    task = PtdTask(1, 'Test task with description and priority',
                   'This is an awesome task with description and priority', 2)

    assert task.id == 1
    assert task.name == 'Test task with description and priority'
    assert task.description == 'This is an awesome task with description and priority'
    assert task.priority == 2
    assert not task.done


def test_task_mark_as_done():
    task = PtdTask(1, 'Test task')
    task.mark_as_done()

    assert task.done

def test_task_comparison():
    task_a = PtdTask(1, 'not important', 'not important task', 100)
    task_b = PtdTask(2, 'important', 'important task', 4)
    task_c = PtdTask(3, 'very important', 'very important task', 1)
    task_d = PtdTask(4, 'important 2', 'important task 2', 4)

    assert task_b < task_a
    assert task_a > task_b
    assert task_c < task_b
    assert task_b > task_c
    assert task_c < task_a
    assert task_a > task_c
    assert task_b == task_d
