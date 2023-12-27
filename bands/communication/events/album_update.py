from bunny_m import BaseEvent

from bands.communication.messages.formats.album_update import AlbumUpdateMessageFormat


class AlbumUpdateEvent(BaseEvent):
    @classmethod
    def get_event_name(cls) -> str:
        return 'album_update'

    @classmethod
    def get_message_format(cls) -> AlbumUpdateMessageFormat:
        return AlbumUpdateMessageFormat()
