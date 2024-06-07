from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

# request body
class Blogs(BaseModel):
    id: int
    title: str
    body: str
    desc: Optional[str] = None

app = FastAPI()

@app.post("/blog")
async def create_blog(blog: Blogs):
# def create_blog(request: Blogs):    
#   return blog
    return {'data': f"Blog is created with title as {blog.title}"}

# for debugging purpose
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5000)