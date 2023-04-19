from dataclasses import dataclass


@dataclass
class TeamDTO:
    name: str
    country_id: int
    sport_type_id: int
    description: str
