from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.init_db import Base
from .deps import AgeRange, association_table

class User(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    state = Column(String)
    address = Column(String)
    interests = relationship(
        'User', 
        secondary=association_table,
        back_popululate= 'Post'
    )
    flags =relationship(
        'User', 
        secondary=association_table,
        back_popululate= 'Post'
    )
    desc =Column(String)
    age_range = Column(Enum(AgeRange))

    def __repr__(self) -> str:
        return f'post: {self.title}'