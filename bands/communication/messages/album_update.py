from dataclasses import dataclass
from datetime import datetime

from bunny_m import Message

from bands.communication.messages import BandUpdateMessage


@dataclass
class AlbumUpdateMessage(Message):
    title: str
    release_date: datetime.date
    artist: BandUpdateMessage
