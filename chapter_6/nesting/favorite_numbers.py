favorite_numbers = {
    "Alice": [7, 10, 21],
    "Bob": [5, 15],
    "Charlie": [3, 8, 12],
    "David": [5, 9, 14],
    "Eve": [23, 2]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers:")

    for number in numbers:
        print(f"\t{number}")
    print()
