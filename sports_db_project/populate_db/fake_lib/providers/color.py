import json
import random


class ColorProvider:
    def __call__(self) -> str:
        with open('data/colors_list.json') as file:
            all_colors = json.load(file)
            random_color = random.choice(all_colors)
            return random_color['name']
