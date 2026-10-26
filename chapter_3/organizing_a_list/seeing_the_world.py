places = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Cairo']
# Original order
print('Original order:')
print(places)

# Alphabetical order
print('\nAlphabetical order:')
print(sorted(places))
print('Original order:')
print(places)

# Reverse alphabetical order
print('\nReverse alphabetical order:')
print(sorted(places, reverse=True))
print('Original order:')
print(places)

# Reverse the list
places.reverse()
print('\nReversed order:')
print(places)

# Reverse the list a gain
places.reverse()
print('\nOriginal order restored:')
print(places)

# Sort alphabetically
places.sort()
print('\nAlphabetical order:')
print(places)

# Sort in reverse alphabetical order
places.sort(reverse=True)
print('\nReverse alphabetical order:')
print(places)
