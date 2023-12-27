from bunny_m import BaseEvent

from bands.communication.messages.formats.concert_update import ConcertUpdateMessageFormat


class ConcertUpdateEvent(BaseEvent):
    @classmethod
    def get_event_name(cls) -> str:
        return 'concert_update'

    @classmethod
    def get_message_format(cls) -> ConcertUpdateMessageFormat:
        return ConcertUpdateMessageFormat()
