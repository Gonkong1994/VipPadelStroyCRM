from fastapi import FastAPI
from client import Client
import json
import os

app = FastAPI(title="VipPadelStroyCRM")

JSON_FILE = "clients.json"


def load_clients():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    return [Client(**item) for item in data]


def save_clients(clients):
    data = [c.model_dump() for c in clients]
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.get("/")
def root():
    return {"message": "VipPadelStroy CRM API is running!"}


@app.get("/clients")
def get_clients():
    return [c.model_dump() for c in load_clients()]


@app.get("/clients/count")
def count_clients():
    return {"total": len(load_clients())}


@app.get("/clients/{name}")
def get_client(name: str):
    for c in load_clients():
        if c.name.lower() == name.lower():
            return c.model_dump()
    return {"error": "Client not found"}


@app.post("/clients")
def create_client(name: str, courts: int = 0, phone: str = ""):
    clients = load_clients()
    new_client = Client(name=name, courts=courts, phone=phone)
    clients.append(new_client)
    save_clients(clients)
    return new_client.model_dump()


@app.put("/clients/{name}")
def edit_client(name: str, courts: int = None, phone: str = None):
    clients = load_clients()
    for c in clients:
        if c.name.lower() == name.lower():
            if courts is not None:
                c.courts = courts
            if phone is not None:
                c.phone = phone
            save_clients(clients)
            return c.model_dump()
    return {"error": "Client not found"}


@app.delete("/clients/{name}")
def remove_client(name: str):
    clients = load_clients()
    for c in clients:
        if c.name.lower() == name.lower():
            clients.remove(c)
            save_clients(clients)
            return {"deleted": name}
    return {"error": "Client not found"}