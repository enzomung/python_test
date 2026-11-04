glossary = {
    'variable': 'A named location used to store data in the memory.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'loop': 'A programming construct that repeats a block of code as long as a specified condition is true.',
    'conditional statement': 'A feature in programming that performs different actions based on whether a specified condition evaluates to true or false.',
    'list': 'A collection of items that are ordered and changeable, allowing duplicate members.',
    'dictionary': 'A collection of key-value pairs that are unordered, changeable, and indexed by unique keys.',
    'tuple': 'An ordered collection of items that is immutable, meaning its elements cannot be changed after creation.',
    'set': 'An unordered collection of unique items that is mutable, allowing for the addition and removal of elements.',
    'string': 'A sequence of characters used to represent text in programming.',
    'integer': 'A whole number without a fractional component, used to represent numerical values in programming.',
}

for word, definition in glossary.items():
    print(f"{word.title()}:\n\t{definition}\n")
