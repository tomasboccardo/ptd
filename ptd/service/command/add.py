from ptd.model.todo import PtdTask
from ptd.service.command.base import PtdBaseCommand


class PtdAddCommand(PtdBaseCommand):
    def execute(self, **kwargs):
        todo_list_name = kwargs.get('todo_list_name', 'default')
        todo_list = self.ptd_app.get_todo_list(todo_list_name)

        task = PtdTask(
            task_id=todo_list.next_id,
            name=kwargs.get('name'),
            description=kwargs.get('description', ''),
            priority=kwargs.get('priority', 5),
        )

        todo_list.add_task(task)
