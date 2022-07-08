"""
    1. class and objects
    2. Inheritance->'IS A' relationship
    3. Polymorphisam
        - method overriding
    4. Abstraction - physically non exsistential 
    (example:- shape itself is not a object but circle,
                rect is a shape)
"""

# class Car:
#     pass

# c = Car()
# c.color = "red"

class Car:#property and behaviour
    #initializer function
    def __init__(self,model,color="blue"):
        self.modl = model
        self.colr = color

    def print(self):
        print(self.modl)
        print(self.colr)
c = Car("XI","black")
del c
c.print()


