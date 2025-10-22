from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Juan", surname="Jose", url="https://jose.com", age=35),
            User(id=2,name="Maria", surname="Del Valle", url="https://delvalle.com", age=35),
            User(id=3,name="Luis", surname="Chacon", url="https://chacon.com", age=33)]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "no se ha encontrado el usuario"}

@router.get("/userquery")
async def userquery(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "no se ha encontrado el usuario"}

@router.post("/user", response_model = User, status_code = 201)
async def add(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(204, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return {"usuario agregado: ": user}

@router.put("/user/")
async def updateUser(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha encontrado el usuario"}

@router.delete("/user/{id}")
async def deleteUser(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}