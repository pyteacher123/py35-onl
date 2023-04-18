import random
from typing import Any


class RandomValueFromListProvider:
    def __init__(self, values: list[Any]) -> None:
        self._values = values
    
    def __call__(self) -> int:
        return random.choice(self._values)[0]
