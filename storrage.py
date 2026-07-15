import json
from client import Client

clients = []
def save_clients(clients):
    data = []
    for client in clients:
        if client.name.isalpha():
            data.append(client.to_dict())
            #print('Client added!')
        else:
            print('Client not added! Please enter Name!')
            
        
    with open('clients.json', 'w') as file:
        json.dump(data,file,indent=4)
            
        
            
def load_clients():
    clients = []
    try:
        with open('clients.json', 'r') as file:
            data = json.load(file)
        for item in data:
            client = Client(
                item['name'],
                item['courts']                
            )            
            
            clients.append(client)
    except FileNotFoundError:
        pass
    return clients