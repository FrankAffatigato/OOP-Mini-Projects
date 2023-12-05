import csv

#Instance and object are referred to as the same thing
'''Hard coding instances objects'''
class Item:
    all = []
    pay_rate = 0.8 # The pay rate after a 20% discount

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity
    
        Item.all.append(self)
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self

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
        #print(items)
        #for instance in instances:
            #items
        
#this is the same as creating an instance of a class

Item.instantiate_instance()
'''
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''
