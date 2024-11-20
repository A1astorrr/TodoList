from fastapi import FastAPI
import uvicorn
from app.todo.views import  router as router_todos

app = FastAPI()
app.include_router(router_todos)


@app.get("/",
         tags=["Приветствие"])
def welcome():
    return {"message": "Welcome to Todo"}


if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)