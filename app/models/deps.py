import enum
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, ForeignKey
from app.db.init_db import Base

association_table= Table(
    'association',
    Base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('post_id', ForeignKey('posts.id'))
)

class AgeRange(enum.Enum):
    pass