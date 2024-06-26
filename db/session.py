

# Управление сессией базы данных
from sqlalchemy import create_engine, select, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from db.models import User
from backend.config import DATABASE_URL
from db.base import Base


engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def make_new_user(name, password):
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    if user is None:
        new_user = User(
            name=name,
            password=password,
        )
        session.add(new_user)
        session.commit()


def get_user(user_name):
    session = Session()
    user = session.query(User).filter_by(name=user_name).first()
    return user


def get_all_user_ids():
    session = Session()
    query = select(User.id)
    result = session.execute(query)
    return [row[0] for row in result.fetchall()]

