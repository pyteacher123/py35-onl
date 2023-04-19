import json
import random


class SportProvider:
    def __call__(self) -> str:
        with open('data/sports_list.json') as file:
            all_sports = json.load(file)
            return random.choice(all_sports)
