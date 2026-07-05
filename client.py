PRICE_PER_COURT = 35000

class Client:   
    
    def __init__(self, name, courts):
        self.name = name
        self.courts = courts
        
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
        self.courts += count
        
    def remove_courts(self, count):
        if self.courts - count >= 0:
            self.courts -= count
        else:
            print('Can not remove so many courts!!')
    
    def to_dict(self):
        return{'name' : self.name, 'courts' : self.courts}