from pet import Pet

class Cat(Pet):
    def __init__(self, name, age, breed, description=""):
        super().__init__(name, age, breed, "Cat", description)

