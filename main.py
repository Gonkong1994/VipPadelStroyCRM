from client import Client
from storrage import save_clients, load_clients

clients = []
save_clients(clients)

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
        
    if choise == "1":
                   
        client_name = input('What is client name? ')
        count_courts = int(input('How mamy courts? '))
        
        client = Client(client_name, count_courts)
        clients.append(client)
        save_clients(clients)
        print('Client added!')
        
    if choise == '2':
        if len(clients) == 0:
            print('You havent clients!')
        for client in clients:
            print('=========\n') 
            client.print_report()
            print('\n=========')
              
            
    if choise == "3":
        ver_name = input("Client name: ").lower()
        print()
        found = False
        for client in clients:
            if ver_name == client.name.lower():
                print("Client found! \n======")
                client.print_report()
                print('=========')   
                found = True
                break
                
        if not found:
            print('Client not found!')
            
    if choise == '4':
        ver_name = input("Client name: ").lower()
        print()
        found = False
        for client in clients:
            if ver_name == client.name.lower():
                print("Client found! \n======")
                client.print_report()
                
                print('1 - Change name')
                print('2 - Add courts')
                print('3 - Remove courts')
        
        
                edit = input('Enter num 1, 2 or 3: ')
                if edit == '1':
                    client.change_name(new_name = input('Enter new name: '))
                    client.show_info()
                    save_clients(clients)
                    continue
            
                if edit == '2':
                    count = int(input('How many courts to add? '))
                    client.add_courts(count)
                    client.show_info()
                    save_clients(clients)
                    continue
                
                if edit == '3':
                    count = int(input('How many courts do you want to remove? '))               
                    client.remove_courts(count)
                    client.show_info()
                    save_clients(clients)
                    continue
                        
                    
                        
                
                print('=========')   
                found = True
                break
                
        if not found:
            print('Client not found!')
            continue
            
        
            
    if choise == '5':
        print('Bye!!!')
        break