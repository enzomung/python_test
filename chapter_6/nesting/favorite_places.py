favorite_places = {
    'david': ['japan', 'korea', 'malaysia'],
    'john': ['paris', 'london'],
    'alex': ['switzerland', 'italy', 'china']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places:")

    for place in places:
        print(f"\t{place.title()}")
    print()
