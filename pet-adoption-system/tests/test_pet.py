import pytest
from src.pet import Pet
from src.dog import Dog
from src.cat import Cat

def test_pet_initialization():
    pet = Pet(name="Buddy", age=3, breed="Golden Retriever", species="Dog", description="Friendly and energetic")
    assert pet.name == "Buddy"
    assert pet.age == 3
    assert pet.breed == "Golden Retriever"
    assert pet.species == "Dog"
    assert pet.description == "Friendly and energetic"

def test_dog_initialization():
    dog = Dog(name="Buddy", age=3, breed="Golden Retriever", description="Friendly and energetic")
    assert dog.name == "Buddy"
    assert dog.age == 3
    assert dog.breed == "Golden Retriever"
    assert dog.species == "Dog"
    assert dog.description == "Friendly and energetic"

def test_cat_initialization():
    cat = Cat(name="Whiskers", age=2, breed="Siamese", description="Loves to nap in the sun")
    assert cat.name == "Whiskers"
    assert cat.age == 2
    assert cat.breed == "Siamese"
    assert cat.species == "Cat"
    assert cat.description == "Loves to nap in the sun"

def test_pet_str_method():
    pet = Pet(name="Bella", age=4, breed="Persian", species="Cat")
    assert str(pet) == "Bella (Cat, Persian, 4 years old)"

def test_dog_display_details(capsys):
    dog = Dog(name="Rex", age=5, breed="Bulldog", description="Strong and loyal")
    dog.display_details()
    captured = capsys.readouterr()
    assert "Name: Rex" in captured.out
    assert "Species: Dog" in captured.out
    assert "Breed: Bulldog" in captured.out
    assert "Age: 5 years" in captured.out
    assert "Description: Strong and loyal" in captured.out

def test_cat_display_details(capsys):
    cat = Cat(name="Luna", age=3, breed="Maine Coon", description="Playful and friendly")
    cat.display_details()
    captured = capsys.readouterr()
    assert "Name: Luna" in captured.out
    assert "Species: Cat" in captured.out
    assert "Breed: Maine Coon" in captured.out
    assert "Age: 3 years" in captured.out
    assert "Description: Playful and friendly" in captured.out
