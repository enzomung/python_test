students = {
    "Alice": {
        'age': 20,
        'favorite_numbers': [7, 10, 2]
    },
    "john": {
        'age': 25,
        'favorite_numbers': [5, 15]
    }
}

for name, information in students.items():
    print(f"\nName: {name.title()}")
    print(f"Age: {information['age']}")
    print("Favorite Number:")

    for number in information['favorite_numbers']:
        print(f"\t{number}")
