from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from typing import Optional


# declarative base class
class Base(DeclarativeBase):
    pass


# Users for the system to access data
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str] 
    middle_name: Mapped[Optional[str]] #Optional for distinguishing users
    last_name: Mapped[str] 
    user_role: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now())

    @property 
    def fullname(self):
        return self.first_name + ' ' + self.last_name


#For managing auth sessions
class Sessions(Base):
    __tablename__ = "sessions"
    id:Mapped[str] = mapped_column(primary_key=True)

#to manage customer information
class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)

#To map user to system to sale for reporting and aggregation
class Sales(Base):
    __tablename__ = "sales"
    id: Mapped[int] = mapped_column(primary_key=True)

#For system logging and view
class Log(Base):
    __tablename__ = 'logs'
    id: Mapped[int] = mapped_column(primary_key=True)