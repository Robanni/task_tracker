from dataclasses import dataclass
from repository import TaskCache , TaskRepository
from schemas.task import TaskSchema

@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache

    def get_tasks(self):
        if tasks := self.task_cache.get_tasks():
            return tasks
        else:   
            tasks = self.task_repository.get_tasks()
            task_schema = [TaskSchema.model_validate(task) for task in tasks]
            self.task_cache.set_tasks(task_schema)
            return tasks