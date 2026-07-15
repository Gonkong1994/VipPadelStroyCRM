


class Client:   
    
    PRICE_PER_COURT = 38000
    DISCOUNT_THESHOLD = 3
    DISCOUNT_PERCENT = 5

    
    def __init__(self, name, courts):
        self.name = name
        self.courts = courts
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Name must be a string, not {type(value).__name__}')
        
        if len(value.strip()) < 2:
            raise ValueError('Name must be at least 2 characters')
        
        
        self._name = value.strip()
        
    @property
    def courts(self) -> int:
        return self._courts
    
    @courts.setter
    def courts(self, value):
        if value >= 0:
            self._courts = value
        else:
            raise ValueError('Count courts cant be a nrgative') 
        
        
    def total_price(self) -> int:
        return self.courts * self.PRICE_PER_COURT
        
    def discount(self) -> int:
        if self.courts >= self.DISCOUNT_THESHOLD:
            return self.DISCOUNT_PERCENT
        else:
            return 0
            
    def final_price(self) -> float:
        price = self.total_price()
        if self.discount():
            return price * (1 - self.DISCOUNT_PERCENT / 100)
            
        else:
            return price
        
    def change_name(self, new_name: str) -> None:
        self.name = new_name
        
    def add_courts(self, count: int) -> None:
        if count <= 0:
            raise ValueError('Count must be a positive')            
        self.courts += count
        
        
    def remove_courts(self, count: int) -> None:
        if count <= 0:
            raise ValueError('Count must be positive')
        
        if count > self._courts:
            raise ValueError('Cannot remove more courts than client has')
        
        self.courts -= count
                   
    
    def to_dict(self) -> dict:
        return{'name' : self.name, 'courts' : self.courts}
    
    def __str__(self) -> str:
        return f"Client(name = '{self.name}', courts = {self.courts})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return False
        return self.name.lower() == other.name.lower()
    
    def print_report(self) -> None:
        print(f'Client : {self.name}')
        print(f'Courts: {self.courts}')
        print(f'Price: {self.total_price()}')
        print(f'Discount: {self.discount()}%')
        print(f'Final price: {self.final_price()}') 