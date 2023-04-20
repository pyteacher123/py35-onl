from dataclasses import dataclass


@dataclass
class SponsorDTO:
    name: str
    country_id: int
    description: str
