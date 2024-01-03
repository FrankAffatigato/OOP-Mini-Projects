from item import Item
from phone import Phone

#item3 = Item("Phone", 500, 5)

#item3.name = 'laptop'

item3 = Item("Phone", 500, 5)
print(item3.name)  # Output: Phone

# This will raise an AttributeError because the property is read-only
item3.name = 'Laptop'
#print(item3.__name)
#this is the same as creating an instance of a class

'''
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''
