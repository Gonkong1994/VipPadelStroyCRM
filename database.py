import psycopg2

DB_CONFIG = {
    "host" : "localhost",
    "database" : "tennis_club",
    "user" : "postgres",
    "password" : "postgres123"
}
    


conn = psycopg2.connect(**DB_CONFIG)


cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS clients;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        courts INTEGER DEFAULT 0,
        phone VARCHAR(20) DEFAULT ''
    );
""")

conn.commit()
print("Clients database READY")

cursor.close()
conn.close()

def add_client(name: str, courts: int = 0, phone: str = ""):
    conn = psycopg2.connect(**DB_CONFIG)
    
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO clients (name, courts, phone) VALUES(%s,%s,%s)",
        (name, courts, phone)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Client {name} added")
    
def get_all_clients():
    conn = psycopg2.connect(**DB_CONFIG)
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM clients;")
    
    clients = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    for client in clients:
        print(client)
        
def find_client_by_name(name: str):
    conn = psycopg2.connect(**DB_CONFIG)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE name = %s", (name,))
    clients = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    print(clients)
    
def update_courts(name:str, new_courts: int):
    conn = psycopg2.connect(**DB_CONFIG)
    
    cursor = conn.cursor()
    cursor.execute("UPDATE clients SET courts = %s WHERE name = %s", (new_courts, name,))
    conn.commit()
    
    
    cursor.close()
    conn.close()
    
    print(f"Courts for client {name} update to {new_courts}")
    
def delete_client(name:str):
    conn = psycopg2.connect(**DB_CONFIG)
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE name = %s", (name,))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Client {name} deleted")



add_client("Тест", 5, "+375291234567")
print("\nВсе клиенты:")
get_all_clients()

find_client_by_name("Тест")

update_courts("Тест", 3)

find_client_by_name("Тест")

delete_client("Тест")


