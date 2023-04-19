import json
import random


class EmailProvider:
    DOMAINS = ('gmail.com', 'ya.ru', 'yahoo.com')

    def __call__(self) -> str:
        with open('data/names_list.json') as file:
            all_names: list[str] = json.load(file)
            random_name = random.choice(all_names).lower()
            return random_name + '@' + random.choice(self.DOMAINS)
