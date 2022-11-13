from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.init_db import Base
from .deps import AgeRange, association_table

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    fullname = Column(String)
    avatar = Column(String)
    age_range = Column(Enum(AgeRange))
    phone = Column(Integer)
    whatsapp_phone = Column(Integer)
    state = Column(Integer)
    posts = relationship(
        'Post', 
        secondary=association_table,
        back_popululate= 'User'
    )

    def __repr__(self) -> str:
        return f'user: {self.fullname}'
