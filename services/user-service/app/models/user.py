from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.mysql import BINARY

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    user_id = Column(
        BINARY(16),
        primary_key=True
    )

    first_name = Column(
        String(25),
        nullable=False
    )

    last_name = Column(
        String(25),
        nullable=False
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True
    )

    created_at = Column(
        TIMESTAMP
    )