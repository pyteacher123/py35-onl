from dataclasses import dataclass


@dataclass
class SneakerDTO:
    model: str
    color: str
    price: float
    producer_id: int
