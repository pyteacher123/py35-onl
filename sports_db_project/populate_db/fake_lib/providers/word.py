import json
import random


class WordProvider:
    def __call__(self) -> None:
        with open('data/words_list.json') as file:
            all_words = json.load(file)
            return random.choice(all_words)
