class Pet:
    def __init__(self, name, age, breed, species, description=""):
        self.name = name
        self.age = age
        self.breed = breed
        self.species = species
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.species}, {self.breed}, {self.age} years old)"

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Description: {self.description}")

