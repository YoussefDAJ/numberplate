import itertools

# Calculate the number of combinations for letters (2 distinct letters)
num_letter_combinations = len(
    list(itertools.combinations("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2))
)

# Calculate the number of combinations for digits (3 distinct digits)
num_digit_combinations = len(list(itertools.combinations("123456789", 3)))

# Calculate the total number of license plates
total_license_plates = num_letter_combinations * num_digit_combinations

# Generate all possible license plates
all_license_plates = [
    "".join(plate[:2]) + "".join(num)
    for plate in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=2)
    for num in itertools.combinations("123456789", 3)
]

# Print the total number of license plates
print("Total Number of License Plates:", total_license_plates)

# Print all generated license plates (if you really want to see them all)
for plate in all_license_plates:
    print(plate)
