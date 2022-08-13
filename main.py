from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("96c6d3f8-fd68-4fd9-831e-2f6af0a7dbe2"),
        first_name="Aditya",
        last_name="Rai",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("d7be33b8-8363-492a-bb99-19b96d47179f"),
        first_name="Sameer",
        last_name="Singh",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("f8441f0a-bd4b-4475-9b0c-aca58f691b0b"),
        first_name="Kunal",
        last_name="Kumar",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "aditya"}


@app.get("/api/v1/users")
async def get_users():
    return db


@app.post("/api/v1/users")
async def create_users(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return user_id
    raise HTTPException(
        status_code=404,
        detail=f"user id : {user_id} not found"
    )


@app.put("/api/v1/user/{user_id}")
async def update_user(user: UserUpdateRequest, user_id: UUID):
    for i in db:
        if i.id == user_id:
            if user.first_name is not None:
                i.first_name = user.first_name
            if user.last_name is not None:
                i.last_name = user.last_name
            if user.middle_name is not None:
                i.middle_name = user.middle_name
            if user.roles is not None:
                i.roles = user.roles
            return i
    raise HTTPException(
        status_code=404,
        detail=f"user id : {user_id} not found"
    )
