PRICE_PER_COURT = 38000

class Client:   
    
    def __init__(self, name, courts):
        self.name = name
        self.courts = courts
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print('Name must be a sring')
            return
        
        if len(value) < 2:
            print('Name is too short')
        
        self._name = value
        
    @property
    def courts(self):
        return self._courts
    
    @courts.setter
    def courts(self, value):
        if value >= 0:
            self._courts = value
        else:
            print('Courts cant be negative')
            self._courts = 0
        
    def show_info(self):
        print('Client: ', self.name)
        print('Courts: ', self.courts)
        
    def total_price(self):
        return self.courts * PRICE_PER_COURT
        
    def discount(self):
        if self.courts >= 3:
            return 5
        else:
            return 0
            
    def final_price(self):
        price = self.total_price()
        if self.discount() == 5:
            return price * 0.95
            
        else:
            return price
        
    def change_name(self, new_name):
        self.name = new_name
        
    def add_courts(self, count):
        if count <= 0:
            print('Cant enter negative num!')
            return
        self.courts += count
        
    def remove_courts(self, count):
        if count > self.courts:
            print('Can not remove so many courts!!')
            return
        self.courts -= count
        
            
    
    def to_dict(self):
        return{'name' : self.name, 'courts' : self.courts}
    
    def print_report(self):
        self.show_info()
        print('Price: ',self.total_price())
        print('Discount: ', self.discount())
        print('Final price: ', self.final_price()) 