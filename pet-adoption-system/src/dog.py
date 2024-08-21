from pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed, description=""):
        super().__init__(name, age, breed, "Dog", description)
