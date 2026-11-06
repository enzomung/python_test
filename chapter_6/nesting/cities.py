cities = {
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'Tokyo is a major technology hub.'
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'Paris is famous for the Eiffel Tower.'
    },
    'london': {
        'country': 'england',
        'population': 8_900_000,
        'fact': 'London is home to Big Ben.'
    }
}

for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
