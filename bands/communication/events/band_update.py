from bunny_m import BaseEvent

from bands.communication.messages.formats.band_update import BandUpdateMessageFormat


class BandUpdateEvent(BaseEvent):
    @classmethod
    def get_event_name(cls) -> str:
        return 'band_update'

    @classmethod
    def get_message_format(cls) -> BandUpdateMessageFormat:
        return BandUpdateMessageFormat()
