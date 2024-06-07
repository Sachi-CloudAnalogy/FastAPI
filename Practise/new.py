from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .hashing import Hash

 
app = FastAPI()
models.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# CREATE
@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, desc=request.desc)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", tags=['blogs'])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# GET DATA
@app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} doesn't exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    return blog

# DELETE
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE 
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist")
    
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    db.refresh(blog)
    return blog

# CREATING USER
@app.post("/user", tags=['user'])     
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    password = request.password.encode('utf-8')
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# GET USER   
@app.get("/user/{id}", response_model=schemas.ShowUser, tags=['user']) 
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} doesn't exist")
    
    return user