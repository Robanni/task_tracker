from redis import Redis

from schemas.task import TaskSchema


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_tasks(self):
        with self.redis as redis:
            tasks_json:list = redis.lrange("tasks", 0, -1) # type: ignore
            tasks: list[TaskSchema] = [TaskSchema.model_validate_json(
                task) for task in tasks_json]
            return tasks

    def set_tasks(self, tasks: list[TaskSchema]):
        tasks_json = [task.model_dump_json() for task in tasks]
        with self.redis as redis:
            redis.lpush("tasks", *tasks_json)
