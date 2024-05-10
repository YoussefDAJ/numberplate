import random


# Function to generate a random letter
def random_letter():
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# Function to generate a random digit (excluding 0)
def random_digit():
    return str(random.randint(1, 9))


# Function to generate a random license plate
def generate_license_plate():
    letters = [random_letter() for _ in range(2)]
    numbers = [random_digit() for _ in range(3)]
    return "".join(letters + numbers)


# Generate and print a random license plate
license_plate = generate_license_plate()
print("Generated License Plate:", license_plate)
