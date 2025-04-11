
from fastapi import Depends

from database.database import get_db
from repository import TaskRepository, TaskCache
from cache import get_redis_connection
from service import TaskService


def get_task_repository() -> TaskRepository:
    db_session = get_db()
    return TaskRepository(db_session)


def get_task_cache_repository() -> TaskCache:
    redis_connection = get_redis_connection()
    return TaskCache(redis_connection)


def get_task_service(
        task_repository: TaskRepository = Depends(get_task_repository),
        task_cache: TaskCache = Depends(get_task_cache_repository),
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        task_cache=task_cache
    )
