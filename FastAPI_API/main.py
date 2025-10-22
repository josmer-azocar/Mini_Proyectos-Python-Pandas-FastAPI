from fastapi import FastAPI
from routers import basic_auth_users, jwt_auth_users, products, users

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
