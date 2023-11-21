from sqlalchemy import *
import sqlalchemy as db
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import vars


class Base(DeclarativeBase):
    pass

class Users(Base):
     __tablename__ = "Users"
     idTelegram: Mapped[str] = mapped_column(primary_key=True)
     Name: Mapped[str] = mapped_column(String(200))
     Username: Mapped[str] = mapped_column(String(200))
     Telephone: Mapped[str] = mapped_column(String(200))
     LastName: Mapped[Optional[str]]

     def __repr__(self) -> str:
         return f"Users(idTelegram={self.idTelegram!r}, Name={self.Name!r},Username={self.Username!r},Telephone={self.Telephone!r}, LastName={self.LastName!r})"


class UsersAccepted(Base):
     __tablename__ = "UsersAccepted"
     IDTelegram: Mapped[str] = mapped_column(primary_key=True)
     Username: Mapped[str] = mapped_column(String(200))
     Accepted: Mapped[Boolean] = mapped_column(Boolean)
     
     def __repr__(self) -> str:
         return f"Users(IDTelegram={self.IDTelegram!r},Username={self.Username!r},Accepted={self.Accepted!r})"


class UsersBans(Base):
     __tablename__ = "UsersBans"
     IDTelegram: Mapped[str] = mapped_column(primary_key=True)
     Username: Mapped[str] = mapped_column(String(200))
     Bans: Mapped[Boolean] = mapped_column(Boolean)
     
     def __repr__(self) -> str:
         return f"Users(IDTelegram={self.IDTelegram!r},Username={self.Username!r},Bams={self.Bans!r})"


class UniqueNum(Base):
     __tablename__ = "UniqueNum"
     UniqueNum: Mapped[str] = mapped_column(primary_key=True)
     Used: Mapped[Boolean] = mapped_column(Boolean)
     
     def __repr__(self) -> str:
         return f"Users(IDTelegram={self.UniqueNum!r},Used={self.Used!r})"


# Create database engine to postgreSQL
engine = create_engine("url_database")
connection = engine.connect()
session = Session(engine)

def createUser():
    with Session(engine) as session:
         Manuel = Users(
             idTelegram="1234567",
             Name="Manuel",
             LastName="Alberto",
             Telephone="+6566",
             Username="@manuel"
         )
         session.add(Manuel)
         session.commit()

def checkExist(idTelegram):#Testing that function not working
    query = db.select(
    db.select(Users).filter_by(idTelegram=idTelegram).exists())
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    print(ResultSet)
    print(ResultSet[0][0])

def isBan(IDTelegram):
    query = db.select(UsersBans)
    query = query.where(IDTelegram == IDTelegram)
    result = connection.execute(query)
    for row in result:
        print(row) 
    
#isBan("123231312")
#checkExist('123231312')
#stmt = select(Users).where(Users.Name.in_(["Manuel", "Alberto"]))
#for user in session.scalars(stmt):
    #print(user)