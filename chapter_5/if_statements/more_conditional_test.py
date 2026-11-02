# 1. String comparisons
name = "Alice"
print(name == "Alice")  # True
print(name == "Bob")    # False

# 2. lower() method
name = "Alice"
print(name.lower() == "alice")  # True
print(name.lower() == "bob")    # False

# 3. Numerical tests
age = 25
print(age == 25)  # True
print(age != 30)  # True
print(age < 30)   # True
print(age > 30)   # False
print(age <= 25)  # True
print(age >= 20)  # True

# 4. and, or operators
print(age > 20 and age < 30)  # True
print(age < 20 or age > 30)  # False

# 5. in operator
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("orange" in fruits)  # False

# 6. not operator
print("apple" not in fruits)  # False
print("orange" not in fruits)  # True
