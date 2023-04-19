import random
from typing import Optional


class DatesRangeProvider:
    def __call__(self) -> tuple[int, Optional[int]]:
        first_date = random.choice(range(1930, 2020))
        second_date = random.choice([random.choice(range(first_date, 2023)), None])
        return first_date, second_date
