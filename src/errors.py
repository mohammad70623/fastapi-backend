from typing import Any, Callable
from fastapi.responses import JSONResponse
from fastapi.responses import Request

class BooklyException(Exception):
    """ This is the base class for all bookly errors """
    pass

class InvalidToken(BooklyException):
    """ User Has provided an invalid or expired token """
    pass  

class RevokedToken(BooklyException):
    """ User Has provided a token that has been revoked """
    pass 

class AccessTokenRequired(BooklyException):
    """ User has provide a refress token when a access token is required """
    pass

class RefreshTokenRequired(BooklyException):
    """ User has provided an access token whena a refresh token is required """
    pass

class UserAlreadyExists(BooklyException):
    """ User has provided an email for a user who exists during sign up """
    pass

class InvalidCredentials(BooklyException):
    """ User has provided wromg email or password during log in"""
    pass

class IssufficientPermission(BooklyException):
    """ User doesnot have the necessery permission to perform an action """
    pass 

class  BookNotFound(BooklyException):
    """ Book Not found """
    pass

class TagNotFound(BooklyException):
    """ Tag Not Found"""
    pass 

class TagAlreadyExists(BooklyException):
    """ Tag Already Exists"""
    pass

class UserNotFound(BooklyException):
    """ User Not Found"""
    pass

def create_exception_handler(status_code: int, initial_detail: Any) -> Callable[[Request, Exception], JSONResponse]:
    
    async def exception_handler(request: Request, exc: BooklyException):
        
        return JSONResponse(
            content=initial_detail,
            status_code=status_code
        )
    
    return exception_handler


