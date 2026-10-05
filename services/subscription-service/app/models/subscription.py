from sqlalchemy import Column, String, Integer, Date, TIMESTAMP
from sqlalchemy.dialects.mysql import BINARY

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Subscription(Base):

    __tablename__ = "subscriptions"

    subscription_id = Column(
        BINARY(16),
        primary_key=True
    )

    subscription_name = Column(
        String(100)
    )

    user_id = Column(
        BINARY(16),
        nullable=False
    )

    plan_id = Column(
        Integer,
        nullable=False
    )

    subscription_type = Column(
        String(25)
    )

    start_date = Column(
        Date,
        nullable=False
    )

    end_date = Column(
        Date
    )

    status = Column(
        String(25),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP
    )

    created_by = Column(
        String(25)
    )