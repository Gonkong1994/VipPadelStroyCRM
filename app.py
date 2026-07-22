from fastapi import FastAPI
from fastapi import Body
from client import Client
from storrage import load_clients
from storrage import save_clients

app = FastAPI(title = "VipPadelStroyCRM")

@app.get("/")
def root():
    return {"message":"VipPadelStroy CRM API is running!"}

@app.get("/clients")
def get_clients():
    clients = load_clients()
    return [client.model_dump() for client in clients]

@app.get("/clients/{name}")
def get_client(name: str):
    clients = load_clients()
    for client in clients:
        if client.name.lower() == name.lower():
            return client.model_dump()
    return {"Error":"Client not found"}

@app.get("/clients/filter/by-courts")
def filter_clients(min_courts: int = 0):
    clients = load_clients()
    result = [c.model_dump() for c in clients if c.courts >= min_courts]
    return result

@app.post("/client")
def create_client(name: str, courts: int = 0, phone: str = ""):
    clients = load_clients()
    new_client = Client(name = name, courts = courts, phone = phone)
    clients.append(new_client)
    save_clients(clients)
    return new_client.model_dump()

@app.delete("/clients/{name}")
def remove_client(name: str):
    clients = load_clients()
    for client in clients:
        if client.name.lower() == name.lower():
            clients.remove(client)
            save_clients(clients)
            return {"Deleted" : name}
    return {"Error":"Client not found"}

@app.put("/clients/{name}")
def edit_client(name:str, courts : int = None, phone: str = None):
    clients = load_clients()
    for client in clients:
        if client.name.lower() == name.lower():
            if courts is not None:
                client.courts = courts
                
            if phone is not None:
                client.phone = phone
                
            save_clients(clients)
            return client.model_dump()
    return {"Error":"Client not found"}  
