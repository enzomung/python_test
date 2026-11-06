person1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

person2 = {
    "first_name": "john",
    "last_name": "wick",
    "age": 25,
    "city": "Kuala lumpur"
}

person3 = {
    "first_name": "alex",
    "last_name": "brown",
    "age": 22,
    "city": "penang"
}

people = [person1, person2, person3]

for person in people:

    print(f"Name: {person['first_name'].title()}"
          f" {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()
