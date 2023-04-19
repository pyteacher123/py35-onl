import json
import random


class SurnameProvider:
    def __call__(self) -> str:
        with open('data/surnames_list.json') as file:
            all_surnames: list[str] = json.load(file)
            return random.choice(all_surnames)
