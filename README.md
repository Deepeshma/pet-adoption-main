# Pet Adoption System

## Project Description

The Pet Adoption System is a command-line application designed to manage the adoption of pets. It allows users to:
- View a list of all available pets
- Add new pets to the system
- Search for pets by type, breed, or age
- Adopt pets, removing them from the available list
- View detailed information about a specific pet
- Save and load pet data to and from CSV files

The system is structured using Object-Oriented Programming principles with a clear separation of classes for pets, specific pet types (Dog and Cat), and the shelter managing the pets.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Deepeshma/pet-adoption-system.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd pet-adoption-system
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Navigate to the `src` directory:**

    ```bash
    cd src
    ```

2. **Run the application:**

    ```bash
    python main.py
    ```

3. **Follow the on-screen prompts to interact with the system.** You can:
    - List all pets
    - Add a new pet
    - Search for pets
    - Adopt a pet
    - Display pet details
    - Save shelter data
    - Load shelter data

## Testing

1. **Navigate to the project directory (if not already there):**

    ```bash
    cd pet-adoption-system
    ```

2. **Ensure the virtual environment is activated (if using one).**

3. **Run the tests using `pytest`:**

    ```bash
    pytest
    ```

4. **View test results to ensure all tests pass and the system functions as expected.**

For more information, refer to the code comments and inline documentation within the source files.
