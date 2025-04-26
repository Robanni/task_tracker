

class UserNotFoundException(Exception):
    details = "User not found"

class UserNotCorrectPasswordException(Exception):
    details = "User not correct password"