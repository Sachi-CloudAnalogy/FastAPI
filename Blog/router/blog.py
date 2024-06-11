from fastapi import APIRouter, Depends, status, HTTPException, Response 
from .. import schemas, models, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
    )

get_db = database.get_db

# TO GET ALL THE RECORDS
@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    # blogs = db.query(models.Blog).all()
    # return blogs

# CREATE
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)
    # new_blog = models.Blog(title=request.title, desc=request.desc, user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog

# GET DATA BY ID 
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {'detail': f"Blog with the id {id} doesn't exist"}
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    # return blog

# DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE 
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")

    # blog.update(request.dict(), synchronize_session=False)
    # db.commit()

    # updated_blog = blog.first()

    # return {
    #     "updated_blog": updated_blog
    # }

    # # db.refresh(blog) 
    # # return blog
