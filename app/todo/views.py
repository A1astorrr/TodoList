from fastapi import APIRouter, HTTPException, status, Depends
from app.todo.crud import TodoDAO
from app.todo.schemas import Todo, TodoBase, TodoCreate, TodoUpdate
from app.exceptions import (
    TodoByIdNotFound,
    TodoCreated,
    TodoDeleted,
    TodoNotCreated,
    TodoNotUpdate,
    TodoUpdated,
    NotDeletedById,
)


router = APIRouter(
    prefix="/todos",
    tags=["Список дел"],
)


@router.get("/", response_model=list[Todo])
async def get_todos(skip: int = 0, limit: int = 100):
    todos = await TodoDAO.get_all()
    return todos[skip : skip + limit]


@router.get("/{todo_id}/", response_model=Todo)
async def get_todo(todo_id: int):
    todo = await TodoDAO.get_id(todo_id)
    if todo is None:
        raise TodoByIdNotFound
    return todo


@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    created = await TodoDAO.add(**todo.model_dump())
    if created is None:
        raise TodoNotCreated
    raise TodoCreated


@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    updated = await TodoDAO.update(
        todo_id, **todo_update.model_dump(exclude_unset=True)
    )
    if updated is None:
        raise TodoNotUpdate
    raise TodoUpdated

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    deleted = await TodoDAO.delete(id=todo_id)
    if deleted is None:
        raise NotDeletedById
    raise TodoDeleted
