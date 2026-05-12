from typing import Any, Callable
from fastapi.responses import JSONResponse
from fastapi.requests import Request  
from fastapi import FastAPI, status
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


def register_all_errors(app: FastAPI):
    app.add_exception_handler(
        UserAlreadyExists,
        create_exception_handler(status.HTTP_403_FORBIDDEN, {
            "message": "User with email already exists",
            "error_code": "user_exists"
        })
    )
    app.add_exception_handler(
        UserNotFound,
        create_exception_handler(status.HTTP_404_NOT_FOUND, {
            "message": "User not found",
            "error_code": "user_not_found"
        })
    )
    app.add_exception_handler(
        BookNotFound,
        create_exception_handler(status.HTTP_404_NOT_FOUND, {
            "message": "Book not found",
            "error_code": "book_not_found"
        })
    )
    app.add_exception_handler(
        InvalidCredentials,
        create_exception_handler(status.HTTP_400_BAD_REQUEST, {
            "message": "Invalid Email Or Password",
            "error_code": "invalid_email_or_password"
        })
    )
    app.add_exception_handler(
        InvalidToken,
        create_exception_handler(status.HTTP_401_UNAUTHORIZED, {
            "message": "Token is invalid or expired",
            "resolution": "Please get a new token",
            "error_code": "invalid_token"
        })
    )
    app.add_exception_handler(
        RevokedToken,
        create_exception_handler(status.HTTP_401_UNAUTHORIZED, {
            "message": "Token has been revoked",
            "resolution": "Please get a new token",
            "error_code": "token_revoked"
        })
    )
    app.add_exception_handler(
        AccessTokenRequired,
        create_exception_handler(status.HTTP_401_UNAUTHORIZED, {
            "message": "Please provide a valid access token",
            "error_code": "access_token_required"
        })
    )
    app.add_exception_handler(
        RefreshTokenRequired,
        create_exception_handler(status.HTTP_403_FORBIDDEN, {
            "message": "Please provide a valid refresh token",
            "error_code": "refresh_token_required"
        })
    )
    app.add_exception_handler(
        IssufficientPermission,
        create_exception_handler(status.HTTP_403_FORBIDDEN, {
            "message": "You do not have permission to perform this action",
            "error_code": "insufficient_permission"
        })
    )
    app.add_exception_handler(
        TagNotFound,
        create_exception_handler(status.HTTP_404_NOT_FOUND, {
            "message": "Tag not found",
            "error_code": "tag_not_found"
        })
    )
    app.add_exception_handler(
        TagAlreadyExists,
        create_exception_handler(status.HTTP_409_CONFLICT, {
            "message": "Tag already exists",
            "error_code": "tag_exists"
        })
    )

    @app.exception_handler(500)
    async def internal_server_error(request, exc):
        return JSONResponse(
            content={"message": "Oops! Something went wrong", "error_code": "server_error"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


