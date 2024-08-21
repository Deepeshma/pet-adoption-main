import csv
import os
from dog import Dog
from cat import Cat

class Shelter:
    def __init__(self):
        self.pets = []

    def load_data(self, file_path):
        """Loads pet data from a CSV file."""
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Species'].lower() == 'dog':
                    pet = Dog(row['Name'], int(row['Age']), row['Breed'], row.get('Description', ''))
                elif row['Species'].lower() == 'cat':
                    pet = Cat(row['Name'], int(row['Age']), row['Breed'], row.get('Description', ''))
                self.add_pet(pet)

    def save_data(self, file_path):
        """Saves current pet data to a CSV file."""
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['Name', 'Species', 'Breed', 'Age', 'Description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for pet in self.pets:
                writer.writerow({
                    'Name': pet.name,
                    'Species': pet.species,
                    'Breed': pet.breed,
                    'Age': pet.age,
                    'Description': pet.description
                })

    def add_pet(self, pet):
        """Adds a new pet to the shelter."""
        self.pets.append(pet)

    def list_pets(self):
        """Lists all pets currently in the shelter."""
        if not self.pets:
            print("No pets available in the shelter.")
            return

        print("\n=== All Pets in the Shelter ===")
        for i, pet in enumerate(self.pets, start=1):
            print(f"{i}. {pet}")
        input("Press Enter to return to the main menu.")

    def search_pet(self, search_by, value):
        """Search for pets by type, breed, or age."""
        results = []
        for pet in self.pets:
            if search_by == "species" and pet.species.lower() == value.lower():
                results.append(pet)
            elif search_by == "breed" and pet.breed.lower() == value.lower():
                results.append(pet)
            elif search_by == "age" and pet.age == int(value):
                results.append(pet)
        return results

    def adopt_pet(self, pet_name):
        """Adopt a pet from the shelter."""
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower():
                self.pets.remove(pet)
                print(f"{pet_name} has been adopted!")
                return
        print(f"Pet named {pet_name} not found.")

    def display_pet_details(self, pet_name):
        """Display details of a specific pet."""
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower():
                pet.display_details()
                return
        print(f"Pet named {pet_name} not found.")
