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
    modify_date: Mapped[datetime] = mapped_column(onupdate=lambda: datetime.now())

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
    first_name: Mapped[str]
    middle_name: Mapped[Optional[str]]
    last_name: Mapped[str]
    source: Mapped[str] #Source from where customer came, another software or could be web/in store/phone
    create_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    modify_date: Mapped[datetime] = mapped_column(onupdate=lambda: datetime.now())


#To map user to system to sale for reporting and aggregation
class Sales(Base):
    __tablename__ = "sales"
    id: Mapped[int] = mapped_column(primary_key=True)


#For system logging and view
class Log(Base):
    __tablename__ = 'logs'

    id: Mapped[int] = mapped_column(primary_key=True)
    log_name: Mapped[str]
    log_type: Mapped[str]
    log_source: Mapped[str]
    log_level: Mapped[str]
    log_message: Mapped[str]
    log_datetime: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
