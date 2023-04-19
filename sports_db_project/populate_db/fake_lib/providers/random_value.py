import random
from typing import Any


class RandomValueFromListProvider:
    def __init__(self, values: list[Any]) -> None:
        self._values = values
    
    def __call__(self) -> int:
        random_value = random.choice(self._values)
        if isinstance(random_value, tuple):
            return random_value[0]
        return random_value
