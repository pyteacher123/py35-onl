import random


class IsTeamProvider:
    def __call__(self) -> bool:
        return random.choice([True, False])
