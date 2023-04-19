import json
import random


class PhoneProvider:
    def __call__(self) -> str:
        with open('data/phone_codes_list.json') as file:
            all_phone_codes = json.load(file)
            random_code = random.choice(all_phone_codes)['code']
            return '+' + random_code + str(random.choice(range(111111111, 999999999)))
