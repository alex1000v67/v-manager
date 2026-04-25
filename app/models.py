from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, Integer, DateTime
from datetime import datetime

class Base(DeclarativeBase):
    pass
class MemoryLog(Base):
    __tablename__ = "memory_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    free_value: Mapped[float] = mapped_column(Float)
    create_at: Mapped[datetime] = mapped_column(DateTime, server_default="now()")
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.free_value!r}, fullname={self.create_at!r})"