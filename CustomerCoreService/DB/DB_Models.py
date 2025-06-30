from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column



# declarative base class
class Base(DeclarativeBase):
    pass


# Users for the system to access data
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str] 
    last_name: Mapped[str] 

    @property 
    def fullname(self):
        return self.first_name + ' ' + self.last_name


#For managing auth sessions
class Sessions(Base):
    __tablename__ = "sessions"

#to manage customer information
class Customer(Base):
    __tablename__ = "customers"

#To map user to system to sale for reporting and aggregation
class Sales(Base):
    __tablename__ = "sales"

#For system logging and view
class Log(Base):
    __tablename__ = 'logs'