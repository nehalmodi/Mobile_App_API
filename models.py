from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey,VARCHAR

class User(Base):
    __tablename__ = 'user'
    phone_no = Column(String(10),primary_key=True)
    name = Column(String(25))
    password = Column(Text, nullable=True)
    email = Column(String(25),nullable=True)
    spam_count = Column(Integer,default=0)

    def __repr__(self):
        return f"<User {self.name}"

class Contact(Base):
    __tablename__ = 'contact'
    phone_no = Column(String(10))
    name = Column(String(25))
    email = Column(String(25),nullable=True)
    spam_count = Column(Integer,default=0)
    user_phone_no = Column(String(10),ForeignKey('user.phone_no'))


    def __repr__(self):
        return f"<User {self.name}"



