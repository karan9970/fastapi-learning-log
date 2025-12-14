from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session

from database import engine,SessionLocal
import models
from schemas import UserCreate,UserLogin,UserResponse
from auth import hash_password,verify_password,create_access_token

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#DB Dependency

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"msg":"Day 5: jwt authentication system"}


#register user

@app.post("/register",response_model=UserResponse)
def register(user:UserCreate,db:Session=Depends(get_db)):
    #check if user exists


    existing_user=db.query(models.User).filter(models.User.email==user.email).first()

    if existing_user:
        raise HTTPException(status_code=400,detail="Email already register")
    hashed_pwd=hash_password(user.password)

    new_user=models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
# Login user

@app.post("/login")
def login(user:UserLogin,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.email==user.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="user not found")
    
    if not verify_password(user.password,db_user.hashed_password):
        raise HTTPException(status_code=401,detail="wrong password")
    
    access_token=create_access_token(data={"sub":db_user.email})

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
