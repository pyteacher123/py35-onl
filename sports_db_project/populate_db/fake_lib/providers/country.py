import json
import random


class CountryProvider:
    def __call__(self) -> str:
        with open('data/countries_list.json') as file:
            all_countries: list[dict[str, str | int]] = json.load(file)
            return random.choice(all_countries)['name']
