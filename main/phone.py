from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        
        #call to super function to have access to all attributes and methods
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero."

        self.broken_phones = broken_phones

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"

        
