

class UserNotFoundException(Exception):
    details = "User not found"

class UserNotCorrectPasswordException(Exception):
    details = "User not correct password"

class TokenExpire(Exception):
    details = "Token has expired"

class TokenNotCorrect(Exception):
    details = "Token is not correct"