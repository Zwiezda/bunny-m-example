from typing import Optional, Type

from bunny_m import BaseMessageFormat, Message
from marshmallow import fields

from bands.communication.messages.album_update import AlbumUpdateMessage
from bands.communication.messages.formats import BandUpdateMessageFormat


class AlbumUpdateMessageFormat(BaseMessageFormat):
    title = fields.Str()
    release_date = fields.Date(format='%m-%d-%Y')
    artist = fields.Nested(BandUpdateMessageFormat())

    @classmethod
    def get_message_class(cls) -> Optional[Type[Message]]:
        return AlbumUpdateMessage
