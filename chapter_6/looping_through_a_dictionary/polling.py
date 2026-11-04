favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people = ['jen', 'sarah', 'edward', 'phil', 'mike', 'anna', 'john']

for person in people:
    if person in favorite_languages:
        language = favorite_languages[person].title()
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")
