import uuid
import bcrypt
from fastapi import HTTPException
from models.user import User
from pydantic_schemas.user_creat import UserCreat

@app.post('/signup')
def signup_user(user : UserCreate):
    # extract the data that is comming from req
    # check if user alredy exist 
    # add the user to the database 

    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400,'User with same email already exist')

    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id = str(uuid.uuid4()), email = user.email, password = hashed_pw, name = user.name)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db