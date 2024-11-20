from app.database import async_session, Base
from sqlalchemy import delete, insert, select
from app.todo.models import Todo

class BaseDAO:
    model =  Base
    
    @classmethod
    async def get_todo(cls, todo_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=todo_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
        
    @classmethod
    async def get_todos(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def get_todo_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            added = cls.model(**data)
            session.add(added)
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            return added
    @classmethod
    async def update(cls, todo_id: int, **data):
        async with async_session() as session:
            updated  = await cls.get_todo(todo_id)
            if updated is None:
                return None
            for key, value in data.items():
                setattr(updated, key, value)
                
            session.add(updated)
            await session.commit()
            return updated
        
    @classmethod
    async def delete(cls, **filter_by):
        async with async_session() as session:
            deleted =  await cls.get_todo_or_none(**filter_by)
            if deleted is None:
                return None
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            return deleted