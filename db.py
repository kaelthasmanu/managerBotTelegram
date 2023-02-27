from sqlalchemy import *
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


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



# Create database engine to postgreSQL
engine = create_engine("postgresql+psycopg2://admin:4dm1n*96@152.206.177.185/tgbot",echo=True)
session = Session(engine)
#stmt = select(Users).where(Users.Name.in_(["spongebob", "sandy"]))
#for user in session.scalars(stmt):
    #print(user)

def createUser():
    with Session(engine) as session:
         Manuel = Users(
             idTelegram="1234567",
             Name="Alberto",
             LastName="Reyes",
             Telephone="+5353190783",
             Username="@manuel"
         )
         session.add(Manuel)
         session.commit()

stmt = select(Users).where(Users.Name.in_(["Manuel", "Alberto"]))
for user in session.scalars(stmt):
    print(user)