from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://root:123@localhost:5432/MigrationsORM')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(50), index=False)
    email = Column(String(50), index=True)

