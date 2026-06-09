#Parent Class
class Phone:
    def __init__(self,price,brand,camera):
        self.__price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying a Phone")

#Child Class        
class SmartPhone(Phone):
    def buy(self):
        print("Buying a SmartPhone")

s=SmartPhone(40000,'Samsung',50)
s.buy()