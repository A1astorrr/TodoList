from app.dao.base import BaseDAO
from app.todo.models import Todo

class  TodoDAO(BaseDAO):
    model = Todo