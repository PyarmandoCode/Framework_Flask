from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Book(Base):
    __tablename__ ='book'

    id = Column(Integer,primary_key=True)
    title=Column(String(250))

    @property
    def serialize(self):
        return {
            'title':self.title,
            'id':self.id
        }

engine = create_engine('sqlite:///Flask_BD//books-collection.db')
Base.metadata.create_all(engine)