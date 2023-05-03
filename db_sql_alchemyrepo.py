from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base

class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    name = Column(String(350), nullable=True)
    year_of_production = Column(Integer(), nullable=True)
    
def db_init():
    db_engine = create_engine('sqlite:///db_movies')