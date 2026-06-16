from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

# 创建FastAPI实例
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/hello/user")
async def hello_user():
    return {"message": "Hello World"}

@app.get("/book/{id}")
async def get_book(id: int = Path(..., gt=0, lt=100)):
    return {"id": id, "title": f"这是第{id}本书。"}

@app.get("/author/{name}")
async def get_author(name: str = Path(..., max_length=10, min_length=2)):
    return {"msg": f"这是{name}的信息。"}

@app.get("/user/{id}")
async def get_user(id: int):
    return {"id": id, "user": f"普通用户 {id}"}

@app.get("/news/news_list")
async def get_news_list(
    skip: int = Query(0, description="跳过的记录数", lt=100),
    limit: int = Query(10, description="返回的记录数")
):
    return {"skip": skip, "limit": limit}

# 注册：用户名和密码->str
class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User):
    return user