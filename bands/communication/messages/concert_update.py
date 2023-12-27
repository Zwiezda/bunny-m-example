from dataclasses import dataclass
from datetime import datetime

from bunny_m import Message

from bands.communication.messages import BandUpdateMessage


@dataclass
class ConcertUpdateMessage(Message):
    location: str
    date: datetime.date
    artist: BandUpdateMessage
