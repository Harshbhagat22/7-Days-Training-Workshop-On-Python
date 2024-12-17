class Car   :     # this is the My Car Class....
    def __init__(self,name,model,milege):
        self.name = name
        self.model = model
        self.milege = milege

    def display(self):
        print(self.name)
        print(self.model)
        print(self.milege)

    def greet(self,name):
        print("Welcome to my car garage -->",name)
    @staticmethod
    def hello():
        print("Good Morning !! ")


c1 = Car("BMW","007",12.7)
c1.display()
c1.greet("Harsh")
c1.hello()

