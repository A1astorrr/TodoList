import datetime
from typing import Annotated
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=func.now(), onupdate=func.now()
)]

class Todo(Base):
    __tablename__ = "todos"
    
    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    completed: Mapped[bool]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]