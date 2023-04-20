from dataclasses import dataclass


@dataclass
class ProfileDTO:
    phone: str
    username: str
    description: str
    age: int
    height: int
    weight: int


@dataclass
class PlayerDTO:
    email: str
    name: str
    surname: str
    country_id: int
    sport_type_id: int
    team_id: int
    profile: ProfileDTO
