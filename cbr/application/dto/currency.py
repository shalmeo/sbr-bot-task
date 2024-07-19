from dataclasses import dataclass


@dataclass
class Currency:
    id: str
    name: str
    value: float
