from app.database import async_session, Base
from sqlalchemy import delete, insert, select
from app.todo.models import Todo

class BaseDAO:
    model =  Base
    
    @classmethod
    async def find_by_id(cls, todo_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=todo_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
        
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            todo_add = cls.model(**data)
            session.add(todo_add)
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            return todo_add
        
    @classmethod
    async def delete(cls, **filter_by):
        async with async_session() as session:
            todo_delete =  await cls.find_one_or_none(**filter_by)
            if todo_delete is None:
                return None
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            return todo_delete