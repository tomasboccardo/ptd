from heapq import heappush, heapify

from ptd.util.exceptions import PtdDuplicatedIdException


class PtdTask(object):
    def __init__(self, task_id, name, description='',
                 priority=5, notify_callback=None):
        self.id = task_id
        self.name = name
        self.description = description
        self._priority = priority
        self.done = False
        self.callback = notify_callback

    def mark_as_done(self):
        self.done = True

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        old_value = self._priority
        self._priority = value
        self.notify(value, old_value)

    def notify(self, new_value, old_value):
        if self.callback is not None:
            self.callback(self.id, new_value, old_value)

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority


class PtdTodoList(object):
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.ids = {}
        self.next_id = 1

    def add_task(self, task):
        if self.ids.get(task.id) is not None:
            raise PtdDuplicatedIdException()

        def priority_change_callback(*args):
            heapify(self.tasks)

        task.callback = priority_change_callback
        heappush(self.tasks, task)
        self.ids[task.id] = task
        self.next_id = max(self.ids.keys()) + 1
