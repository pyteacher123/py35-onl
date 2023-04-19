import json
import random


class CompanyProvider:
    def __call__(self) -> str:
        with open('data/companies_list.json') as file:
            all_companies = json.load(file)
            return random.choice(all_companies)
