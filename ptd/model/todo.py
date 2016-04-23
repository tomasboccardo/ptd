class PtdTask(object):
    def __init__(self, task_id, name, description='', priority=5):
        self.id = task_id
        self.name = name
        self.description = description
        self.priority = priority
        self.done = False

    def mark_as_done(self):
        self.done = True

    def __cmp__(self, other):
        if self.priority < other.priority:
            return -1
        elif self.priority == other.priority:
            return 0
        else:
            return 1


class PtdTodoList(object):
    def __init__(self, name):
        self.name = name
        self.tasks = []
