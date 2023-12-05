#Instance and object are referred to as the same thing
'''Hard coding instances objects'''
class Item:
    pay_rate = 0.8 # The pay rate after a 20% discount

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self

#this is the same as creating an instance of a class
item1 = Item("Phone", 100, 5)



'''
#creating another instance
item2 = Item()
item2.name = "laptop"
item2.price = 1000
item2.quanity = 3
'''
print(item1.name)
print(item1.calculate_total_price())
print(item1.price)
print(item1.apply_discount().calculate_total_price())
print(item1.price)
