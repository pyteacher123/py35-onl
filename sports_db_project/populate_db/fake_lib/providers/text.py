import json
import random


class TextProvider:
    def __call__(self) -> str:
        with open('data/words_list.json') as file:
            all_words = json.load(file)
            number_of_words = random.choice(range(8, 20))
            return " ".join([random.choice(all_words) for _ in range(number_of_words)])
