from dataclasses import dataclass
import datetime as dt

from exception import TokenExpire, TokenNotCorrect, UserNotCorrectPasswordException, UserNotFoundException
from models import UserProfile
from repository import UserRepository
from schemas import UserLoginSchema
from jose import JWTError, jwt

from settings import Settings


@dataclass
class AuthService:
    user_repository: UserRepository
    settings: Settings

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username=username)
        user = self._validate_auth_user(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile | None, password: str) -> UserProfile:
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException
        return user

    def generate_access_token(self, user_id: int) -> str:
        expires_date_unix = (dt.datetime.utcnow() +
                             dt.timedelta(days=7)).timestamp()

        token = jwt.encode(
            {'user_id': user_id, 'expire': expires_date_unix},
            key=self.settings.JWT_SECRET_KEY, algorithm=self.settings.JWT_ENCODE_ALGORITHM
        )

        return token

    def get_user_id_from_access_token(self, access_token: str) -> int:
        try:

            payload = jwt.decode(token=access_token, key=self.settings.JWT_SECRET_KEY,
                                algorithms=self.settings.JWT_ENCODE_ALGORITHM)
        except JWTError:
            raise TokenNotCorrect
        if payload['expire'] < (dt.datetime.utcnow()).timestamp():
            raise TokenExpire
        
        return payload['user_id']
