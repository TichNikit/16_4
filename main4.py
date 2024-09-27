from typing import Annotated, List
from fastapi import FastAPI, Path, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()
# users = {'1': 'Имя: Example, возраст: 18'}
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.post('/user/{username}/{age}')
async def create_user(user: User, username: str, age: int):
    user.id = 1 if not users else users[-1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    print(users)
    return user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str, age: int, user: str = Body()):
    try:
        edit_user = users[user_id-1]
        print(edit_user)
        edit_user.username = username
        edit_user.age = age
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        user = users.pop(user_id-1)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.get('/user')
async def get_user():
    return users
