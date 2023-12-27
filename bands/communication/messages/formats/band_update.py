from typing import Optional, Type

from bunny_m import BaseMessageFormat, Message
from marshmallow import fields

from bands.communication.messages.band_update import BandUpdateMessage


class BandUpdateMessageFormat(BaseMessageFormat):
    name = fields.Str()
    email = fields.Email()
    site = fields.Url()

    @classmethod
    def get_message_class(cls) -> Optional[Type[Message]]:
        return BandUpdateMessage
