from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "f23943811630ad5cb3b8b2d1787acb0dbc7b55911bacf9b21552c9615957f8c6"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30


fake_db = {
    "Manuel": {
        "username": "Manuel",
        "full_name": "Manuel Dominguez",
        "email": "manuel@gmail.com",
        "hashed_password": "",
        "disabled": False
    }
}

class Token(BaseModel):
    acces_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str
    
class User(BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    disabled: bool or None = None
    
class UserInDB(User):
    hashed_password: str 
    

pwd_context = CryptContext(schemes=["bcrypt"], depreacted="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()               