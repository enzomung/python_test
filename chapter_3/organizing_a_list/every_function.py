countries = ['USA', 'Canada', 'Germany', 'France', 'Japan']

# Print the list
print(f"Original list: {countries}")

# Modify an element in the list
countries[2] = 'Italy'
print(f"Modified list: {countries}")

# Add a new element to the list
countries.append('Australia')
print(f"List after adding a new country: {countries}")

# Remove an element from the list
countries.remove('France')
print(f"List after removing a country: {countries}")

# Insert a new item
countries.insert(1, 'Spain')
print(f"List after inserting a new country: {countries}")

# Pop an item
popped_country = countries.pop()
print(f"Popped country: {popped_country}")
print(f"List after popping a country: {countries}")

# Delete an item
del countries[-3]
print(f"List after deleting an item: {countries}")

# sort the list
countries.sort()
print(f"Sorted list: {countries}")

# Reverse the list
countries.reverse()
print(f"Reversed list: {countries}")

# Sort Alphabetically
countries.sort()
print(f"Alphabetically sorted list: {countries}")

# Sort in reverse alphabetical order
countries.sort(reverse=True)
print(f"Reverse alphabetically sorted list: {countries}")

# Find the length
print(f"Number of countries in the list: {len(countries)}")
