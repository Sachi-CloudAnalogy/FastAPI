from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from ..hashing import Hash

def create(request: schemas.User, db: Session):
    password = request.password.encode('utf-8')
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} doesn't exist")
    
    return user

 