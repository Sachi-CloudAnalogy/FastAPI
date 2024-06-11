#pydantic models are called schemas
from pydantic import BaseModel
from typing import List, Optional

#pydantic model
class BlogBase(BaseModel):
    title: str
    desc: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blog: List[Blog] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    title: str
    desc: str
    creator: ShowUser
    
    class Config():
        orm_mode = True  

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str 

class TokenData(BaseModel):
    email: Optional[str] = None
    
           