import json
import random


class NameProvider:
    def __call__(self) -> str:
        with open('data/names_list.json') as file:
            all_names: list[str] = json.load(file)
            return random.choice(all_names)
