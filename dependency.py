
from fastapi import Depends, HTTPException, Request, Security, security
from sqlalchemy.orm import Session

from database import get_db
from exception import TokenExpire, TokenNotCorrect
from repository import TaskRepository, TaskCache
from cache import get_redis_connection
from repository import UserRepository
from service import TaskService
from service import UserService
from service import AuthService
from settings import Settings


def get_task_repository(db_session: Session = Depends(get_db)) -> TaskRepository:
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


def get_user_repository(db_session: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository),

) -> AuthService:
    return AuthService(user_repository=user_repository, settings=Settings())


def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository),
        auth_service: AuthService = Depends(get_auth_service)

) -> UserService:
    return UserService(user_repository=user_repository, auth_service=auth_service)


reusable_oauth2 = security.HTTPBearer()


def get_request_user_id(
        auth_service: AuthService = Depends(get_auth_service),
        token: security.http.HTTPAuthorizationCredentials = Security(
            reusable_oauth2)
) -> int:
    try:
        user_id = auth_service.get_user_id_from_access_token(token.credentials)
    except TokenExpire as e:
        raise HTTPException(
            status_code=401,
            detail=e.details
        )
    except TokenNotCorrect as e:
        raise HTTPException(
            status_code=401,
            detail=e.details
        )
    return user_id
