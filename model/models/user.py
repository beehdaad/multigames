from sqlalchemy import ( 
    sql,
    Column,
    Integer,
    String,
)
from model import db


class UserModels(db.Base):
    __tablename__ = "account_users"

    id = Column(
        Integer,
        primary_key=True
    )
    username = Column(
        String(255),
        nullable=False,
        unique=True
    )
    password = Column(
        String(255),
        nullable=False

    )
    wallet = Column(
        Integer,
        nullable=False
    )


if __name__ == "__main__":
    ...