from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user 

router = APIRouter(
    prefix="/user",
    tags=['Users']
    )

get_db = database.get_db

# CREATING USER
@router.post("/")     
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
    # password = request.password.encode('utf-8')
    # new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user

# GET USER
@router.get("/{id}", response_model=schemas.ShowUser) 
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} doesn't exist")
    
    # return user
