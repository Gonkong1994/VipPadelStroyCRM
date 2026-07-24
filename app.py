from fastapi import FastAPI
from storrage import Session, ClientDB
from client import Client


app = FastAPI(title = "VipPadelStroyCRM")

def db_to_pydantic(db_client):
    if db_client is None:
        return None
    return Client(
        name = db_client.name,
        courts = db_client.courts,
        phone = db_client.phone or ""
        )
        
    

@app.get("/")
def root():
    return {"message":"VipPadelStroy CRM API is running!"}

@app.get("/clients")
def get_clients():
    session = Session()
    db_clients = session.query(ClientDB).all()
    session.close()
    return [db_to_pydantic(c).model_dump() for c in db_clients]

@app.get("/clients/count")
def count_clients():
    session = Session()
    count = session.query(ClientDB).count()
    session.close()
    return {"total": count}

@app.get("/clients/{name}")
def get_client(name: str):
    session = Session()
    db_client = session.query(ClientDB).filter(ClientDB.name == name).first()
    session.close()
    if db_client:
        return db_to_pydantic(db_client).model_dump()
    return {"Error":"Client not found"}

@app.get("/clients/filter/by-courts")
def filter_clients(min_courts: int = 0):
    session = Session()
    db_clients = session.query(ClientDB).filter(ClientDB.courst >= min_courts).all()
    session.close()
    return [db_to_pydantic(c).model_dump() for c in db_clients]

@app.post("/clients")
def create_client(name: str, courts: int = 0, phone: str = ""):
    session = Session()
    db_client = ClientDB(name = name, courts = courts, phone = phone)
    session.add(db_client)
    session.commit()
    result = db_to_pydantic(db_client).model_dump()
    session.close()
    return result

@app.delete("/clients/{name}")
def remove_client(name: str):
    session = Session()
    db_client = session.query(ClientDB).filter(ClientDB.name == name).first()
    if db_client:
        session.delete(db_client)
        session.commit()
        session.close()
        return {"deleted" : name}
    session.close()
    return {"error":"Client not found"}



@app.put("/clients/{name}")
def edit_client(name:str, courts : int = None, phone: str = None):
    session = Session()
    db_client = session.query(ClientDB).filter(ClientDB.name == name).first()
    if db_client:
        if courts is not None:
            db_client.courts = courts
        
        if phone is not None:
            db_client.phone = phone
        session.commit()
        result = db_to_pydantic(db_client).model_dump()
        session.close()
        return result
    session.close()
    return {"error":"Client not found"}
