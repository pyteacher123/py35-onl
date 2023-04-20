from dataclasses import dataclass


@dataclass
class ProducerDTO:
    country_id: int
    name: str
    description: str
