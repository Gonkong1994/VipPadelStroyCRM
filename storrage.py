import json
from client import Client

clients = []
def save_clients(clients):
    data = [client.model_dump() for client in clients]
    
       
        
            
        
    with open('clients.json', 'w') as file:
        json.dump(data,file,indent=4)
            
        
            
def load_clients():
    clients = []
    try:
        with open('clients.json', 'r') as file:
            data = json.load(file)
        for item in data:
            client = Client(
                name = item['name'],
                courts = item['courts']                
            )            
            
            clients.append(client)
    except FileNotFoundError:
        pass
    return clients