import json
import random


class SportwareCompanyProvider:
    def __call__(self) -> str:
        with open('data/sportware_companies_list.json') as file:
            all_companies: list[str] = json.load(file)
            return random.choice(all_companies)
