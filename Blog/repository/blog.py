from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status, Response

#GET ALL THE BLOGS
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

# CREATE BLOG
def create(request: schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, desc=request.desc, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#DELETE BLOG
def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE BLOG
def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    
    # original_blog = blog.first()
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    updated_blog = blog.first()

    return {
        # "original_blog": original_blog,
        "updated_blog": updated_blog
    }

#SHOW BLOG BY ID
def show(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} doesn't exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    return blog