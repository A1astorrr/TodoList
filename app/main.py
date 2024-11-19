from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/",
         tags=["Приветствие"])
def welcome():
    return {"message": "Welcome to Todo"}


if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)