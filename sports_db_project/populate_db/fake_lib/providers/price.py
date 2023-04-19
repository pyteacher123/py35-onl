import random


class PriceProvider:
    def __call__(self) -> int:
        return random.choice(range(10, 200))
