class Fruit:
    # Default constructor
    def __init__(self, color):
        self.color = color  

# Derived class
class Store(Fruit):                  # A -> B     # Single level Inheritance...
    def eat(self, name):
        print("The Fruit is = ",name)  


class customer(Store):
    def buy(slef,prize):
        print("The price of Fruit is = ",prize)

c1 = customer("Orange")   # Multi-level Inheritance...  A -> B -> C
print("The colour is = ",c1.color)
c1.eat("Apples")
c1.buy(150)