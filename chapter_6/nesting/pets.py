pet1 = {
    'animal': 'dog',
    'owner': 'david'
}

pet2 = {
    'animal': 'cat',
    'owner': 'john'
}

pet3 = {
    'animal': 'rabbit',
    'owner': 'alex'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"animal: {pet['animal'].title()}")
    print(f"owner: {pet['owner'].title()}")
    print()
