from dataclasses import dataclass


@dataclass
class SportDTO:
    name: str
    is_team: bool
