from pydantic import BaseModel


class UserRegisterDAO:
    username: str
    email: str
    first_name: str = None
    last_name: str = None