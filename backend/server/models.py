from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime


class Poem(Base):
    __tablename__ = 'poems'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))

# class Poem(Base):
#     __tablename__ = 'poems'

#     id = Column(Integer, primary_key=True, nullable=False)
#     title = Column(String(50), nullable=False, unique=True)
#     content = Column(Text(), nullable=False)
#     created_at = Column(DateTime(), default=datetime.utcnow)