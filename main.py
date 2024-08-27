from fastapi import FastAPI

from Session import Session
from models.model import User

app = FastAPI()


@app.get("/user/{user_id}")
async def get_user(user_id):
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()

    print(user.username)
    return {"message": "Hello World"}


@app.put("/user/{user_id}")
async def update_user(user_id):
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()
    user.username = "Manh"
    session.commit()
    print(user.username)
    return {"message": "Hello World"}

@app.post("/users")
async def root():
    user = User(
        user_id=100023,
        username='Toai',
        email='toai@gmail.com',
        password='123',
    )

    session = Session()
    session.add(user)
    session.commit()
    return {
        "user": user.user_id
    }

@app.delete("/users/{user_id}")
async def del_user(user_id):
    session = Session()
    user = session.query(User).filter(User.user_id == user_id).first()
    session.delete(user)
    session.commit()
    return {"status": "del success"}
