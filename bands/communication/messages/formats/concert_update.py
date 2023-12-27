from typing import Optional, Type

from bunny_m import BaseMessageFormat, Message
from marshmallow import fields

from bands.communication.messages.concert_update import ConcertUpdateMessage
from bands.communication.messages.formats import BandUpdateMessageFormat


class ConcertUpdateMessageFormat(BaseMessageFormat):
    location = fields.Str()
    date = fields.Date(format='%m-%d-%Y')
    artist = fields.Nested(BandUpdateMessageFormat())

    @classmethod
    def get_message_class(cls) -> Optional[Type[Message]]:
        return ConcertUpdateMessage
