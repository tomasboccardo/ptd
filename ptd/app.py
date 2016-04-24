from ptd.model.todo import PtdTodoList


class PtdApp(object):
    def __init__(self):
        self.todo_lists = {
            'default': PtdTodoList('default')
        }

    def run_command(self, command):
        print(command)

    def get_todo_list(self, list_name):
        return self.todo_lists.get(list_name)
