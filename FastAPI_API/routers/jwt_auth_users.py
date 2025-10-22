from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "201d6573b0d7d1344a3a3bfe5550b69102fd11be2db6d379588b6ccc58ca230b"

router = APIRouter()
OAuth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "disabled": False,
        "password": "123456"
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "disabled": True,
        "password": "123456"
    }
}

def search_user_db(username: str):
    if username in users_db: 
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db: 
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(OAuth2)):
    
    exception = HTTPException(
                status_code = 401,
                detail="Credenciales de autenticación inválidas",
                headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception    
    except JWTError:
        raise exception
    
    return search_user(username)
        

async def current_user(user: User = Depends(OAuth2)):
    if user.disabled:
        raise HTTPException(
            status_code = 400,
            detail="Usuario inactivo")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(400, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    
    if not user or not crypt.verify(form.password, user.password):
        raise HTTPException(400, detail="La contraseña no es correcta")
    
    access_token = {"sub": user.username,
                "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

