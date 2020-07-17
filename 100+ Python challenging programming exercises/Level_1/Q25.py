"""
Question:
    Define a class, which have a class parameter and have a same instance parameter.
"""

class Bike:
    
    name = "Jack"

    def __init__(self, name):
        self.name = name


adidas = Bike("Leonardo")

print(adidas.name)
print(Bike.name)