import os
from shelter import Shelter

def main():
    shelter = Shelter()

    # Load the data from the pets.csv file inside the data folder
    data_folder = os.path.join(os.path.dirname(__file__), '../data')
    csv_file_path = os.path.join(data_folder, 'pets.csv')
    shelter.load_data(csv_file_path)

    while True:
        print("\n=== Pet Adoption System ===")
        print("1. List all pets")
        print("2. Add a new pet")
        print("3. Search for a pet")
        print("4. Adopt a pet")
        print("5. Display pet details")
        print("6. Save shelter data")
        print("7. Load shelter data")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            shelter.list_pets()
        elif choice == '2':
            name = input("Enter pet's name: ")
            species = input("Enter pet's species (Dog/Cat): ").capitalize()
            breed = input("Enter pet's breed: ")
            age = int(input("Enter pet's age: "))
            description = input("Enter a description for the pet: ")
            
            if species == 'Dog':
                pet = Dog(name, age, breed, description)
            elif species == 'Cat':
                pet = Cat(name, age, breed, description)
            shelter.add_pet(pet)
        elif choice == '3':
            search_by = input("Search by species, breed, or age? ").lower()
            value = input(f"Enter {search_by}: ")
            results = shelter.search_pet(search_by, value)
            if results:
                print("\n=== Search Results ===")
                for pet in results:
                    print(pet)
            else:
                print("No matching pets found.")
        elif choice == '4':
            pet_name = input("Enter the name of the pet to adopt: ")
            shelter.adopt_pet(pet_name)
        elif choice == '5':
            pet_name = input("Enter the name of the pet to display details: ")
            shelter.display_pet_details(pet_name)
        elif choice == '6':
            save_file_path = input("Enter the file path to save data: ")
            shelter.save_data(save_file_path)
        elif choice == '7':
            load_file_path = input("Enter the file path to load data: ")
            shelter.load_data(load_file_path)
        elif choice == '8':
            print("Thank you for using the Pet Adoption System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
