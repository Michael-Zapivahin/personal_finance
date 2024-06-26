from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase
from backend.config import DATABASE_URL



class Base(DeclarativeBase):
    pass


engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Модель Пользователя (User)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    # Другие поля по необходимости

    transactions = relationship("Transaction", back_populates="owner")
    categories = relationship("TransactionCategory", back_populates="owner")


# Модель Категории Транзакций (TransactionCategory)
class TransactionCategory(Base):
    __tablename__ = "transaction_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # Можно использовать Enum для ограничения значений
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category")


# Модель Транзакции (Transaction)
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL(10, 2))
    description = Column(String, nullable=True)
    date = Column(Date)
    category_id = Column(Integer, ForeignKey("transaction_categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("TransactionCategory", back_populates="transactions")
    owner = relationship("User", back_populates="transactions")


# Создание таблиц в базе данных (если они еще не созданы)
Base.metadata.create_all(bind=engine)
