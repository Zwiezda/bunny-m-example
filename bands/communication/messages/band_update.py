from dataclasses import dataclass

from bunny_m import Message


@dataclass
class BandUpdateMessage(Message):
    name: str
    email: str
    site: str
