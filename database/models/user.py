from sqlalchemy import ( 
    sql,
    Column,
    Integer,
    String,
)
from database import db


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

    def __init__(self, username: str, password: str, wallet: int  ) -> None:
        self.username = username
        self.password = password
        self.wallet = wallet
    


    @classmethod
    def register(cls, username: str, password: str):
        user = sql.insert(cls).values(username=username, password=password, wallet=50)
        db.session.execute(user)
        db.session.commit()
        return user

    @classmethod
    def login(cls, username: str, password: str):
        stmt = sql.select(cls).where(cls.username==username, cls.password==password)
        account = db.session.execute(stmt)
        return account.one_or_none()

    @classmethod
    def update_wallet(cls, username, wallet: int):
        stmt = sql.update(cls).where(cls.username==username).values(wallet = wallet)
        db.session.execute(stmt)
        db.session.commit()

    def __str__(self):
        pass

    def __repr__(self):
        pass

if __name__ == "__main__":
    ...