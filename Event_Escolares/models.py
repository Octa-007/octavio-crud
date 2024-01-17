from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

class eventos(Database):
    __tablename__ = 'Eventos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    fecha = Column(String(10))
    lugar = Column(String(10))
    
