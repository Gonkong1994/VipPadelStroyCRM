from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:postgres123@db:5432/tennis_club"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind = engine)

class Base(DeclarativeBase):
    pass

class ClientDB(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    courts = Column(Integer, default = 0)
    phone = Column(String(20), default = "")
    
Base.metadata.create_all(engine)
                  
            
def load_clients():
   session = Session()
   clients = session.query(ClientDB).all()
   session.close()
   return clients