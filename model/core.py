from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from painless import Singleton

class SQLalchemy(metaclass=Singleton):
    def __init__(self) -> None:
        self.engine = self.create_engine()
        self.Base = declarative_base()
        self.session = self.create_session()
    
    def create_engine(self):
        engine = create_engine("sqlite:///multigames.db")
        return engine

    def create_session(self):
        return Session(self.engine)
