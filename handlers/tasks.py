from typing import Annotated
from fastapi import APIRouter, Depends


from dependency import get_request_user_id, get_task_cache_repository, get_task_repository, get_task_service
from repository import TaskCache
from schemas.task import TaskSchema
from repository import TaskRepository
from service import TaskService

router = APIRouter(prefix="/task", tags=["task"])


@router.get(
    "/all",
    response_model=list[TaskSchema],
)
async def get_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)]
):
    return task_service.get_tasks()


@router.post(
    "/",
    response_model=TaskSchema,
)
async def create_task(
    task: TaskSchema,
    task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
    user_id: int = Depends(get_request_user_id)
):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskSchema,
)
async def patch_task(
    task_id: int,
    name: str,
    task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    return task_repository.update_task_name(task_id, name)


@router.delete(
    "/{task_id}",
)
async def delete_task(task_id: int, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task_repository.delete_task(task_id)
    return {"msg": "task was deleted"}
