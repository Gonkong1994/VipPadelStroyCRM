from client import Client
from storrage import save_clients, load_clients
from pydantic import ValidationError

def find_client(clients, name):
    for client in clients:
        if client.name.lower() == name.lower():
            return client
    return None


while True:
    print()
    print('======VipPadelStroy======')
    print('1 - Add client')
    print('2 - Show clients')
    print('3 - Search clients')
    print('4 - Edit client')
    print('5 - Exit')
    
    clients = load_clients()
    
    choise = input("Choise: ")
    print()
    
    if choise not in ('1', '2', '3', '4', '5'):
        print('Unknown command')
        continue
    
    try:    
        if choise == "1":
                    
            client_name = input('What is client name? ')
            phone_number = input('Enter you phone number: ')
            count_courts = int(input('How mamy courts? '))
            
            client = Client(name = client_name, courts = count_courts, phone = phone_number)
            clients.append(client)
            save_clients(clients)
            #print('Client added!')
    except(ValueError, ValidationError) as e:
        print (f'Error: {e}')
        
        
    if choise == '2':
        if len(clients) == 0:
            print('You havent clients!')
        for client in clients:
            print('=========\n') 
            client.print_report()
            print('\n=========')
              
            
    if choise == "3":
        client = find_client(clients, input('Client name: '))        
        if client:
            client.print_report()
        else:
            print('Client not found')
        
        
            
    if choise == '4':
        
        client = find_client(clients, input('Client name: '))
        if client:
            print("Client found! \n======")
            client.print_report()
            print()
            print('1 - Change name')
            print('2 - Add courts')
            print('3 - Remove courts')
            print('4 - Change phone number')
            edit = input('Enter num 1, 2, 3 or 4: ')
           
            if edit == '1':
                try:
                    old_name = client.name
                    client.change_name(new_name = input('Enter new name: '))
                    client.print_report()
                    save_clients(clients)
                    
                except(ValidationError, ValueError) as e:
                    client.name = old_name
                    print(f'Error: {e}')
                continue
            
            if edit == '2':
                    count = int(input('How many courts to add? '))
                    client.add_courts(count)
                    client.print_report()
                    save_clients(clients)
                    continue
                
            if edit == '3':
                    count = int(input('How many courts do you want to remove? '))               
                    client.remove_courts(count)
                    client.print_report()
                    save_clients(clients)
                    continue   
                
            if edit == '4':
                try:
                    old_phone_number = client.phone
                    client.change_phone(new_phone = input('Enter you new phone number: '))                             
                    client.print_report()
                    save_clients(clients)
                except(ValueError,ValidationError) as e:
                    client.phone = old_phone_number
                    print(f'Error: {e}')
                continue                       
                
            print('=========')
            
        else:
            print('Client not found')                                                                    
    if choise == '5':
        print('Bye!!!')
        break