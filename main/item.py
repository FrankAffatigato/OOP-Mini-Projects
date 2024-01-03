import csv

#Instance and object are referred to as the same thing
'''Hard coding instances objects'''
class Item:
    all = []
    pay_rate = 0.8 # The pay rate after a 20% discount

    def __init__(
            self, 
            name: str, 
            price: float, 
            quantity: int = 0
            ):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
    
        self.__name = name
        self.__price = price
        self.quantity = quantity
    
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 15:
            raise Exception("Length of name is too long, must be 15 characters or less")
        else:
            self.__name = value

    @property
    # Property Decorator = Read-Only Attribute
    def price(self):
        return self.__name

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        return self
    
    def apply_increment(self, value):
        self.__price = self.__price + self.__price * value
        if self.__price.is_integer() == True:
            self.__price = int(self.__price)
        else:
            self.__price
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"

    def calculate_total_price(self):
        return self.__price * self.quantity
    

    @classmethod
    def instantiate_instance(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    