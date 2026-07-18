from typing import ClassVar
from pydantic import BaseModel, Field, field_validator


class Client(BaseModel):   
    
    PRICE_PER_COURT: ClassVar[int] = 38000
    DISCOUNT_THESHOLD: ClassVar[int] = 3
    DISCOUNT_PERCENT: ClassVar[int] = 5
    
    name: str = Field(..., min_length = 2, description = 'Client name')
    courts: int = Field(default = 0, ge = 0, description = 'Count courts')
    phone: str = Field(default = '', pattern = r'^|\+?\d{10,15}$')        
        
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
        
    def change_phone(self, new_phone: str) -> None:
        self.phone = new_phone
        
    def add_courts(self, count: int) -> None:
        if count <= 0:
            raise ValueError('Count must be a positive')            
        self.courts += count
        
        
    def remove_courts(self, count: int) -> None:
        if count <= 0:
            raise ValueError('Count must be positive')
        
        if count > self.courts:
            raise ValueError('Cannot remove more courts than client has')
        
        self.courts -= count
                   
    

    
    def __str__(self) -> str:
        return f"Client(name = '{self.name}', courts = {self.courts})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return False
        return self.name.lower() == other.name.lower()
    
    def print_report(self) -> None:
        print(f'Client : {self.name}')
        print(f'Number Phone: {self.phone}')
        print(f'Courts: {self.courts}')
        print(f'Price: {self.total_price()}')
        print(f'Discount: {self.discount()}%')
        print(f'Final price: {self.final_price()}') 