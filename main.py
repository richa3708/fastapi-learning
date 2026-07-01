from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Richa! Welcome to FastAPI"}

@app.get("/about")
def about():
    return{"framework": "FastAPI"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
def search(name: str):
    return {"name": name}