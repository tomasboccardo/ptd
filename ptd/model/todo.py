class PtdTask(object):
    def __init__(self, task_id, name, description='', priority=1):
        self.id = task_id
        self.name = name
        self.description = description
        self.priority = priority
        self.done = False

    def mark_as_done(self):
        self.done = True


class PtdTodoList(object):
    def __init__(self):
        pass