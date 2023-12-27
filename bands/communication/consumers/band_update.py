from abc import ABC, abstractmethod
from typing import Type

from bunny_m import BaseEvent, BaseConsumer

from bands.communication.events.band_update import BandUpdateEvent
from bands.communication.messages.band_update import BandUpdateMessage


class BandUpdateBaseConsumer(BaseConsumer, ABC):
    @classmethod
    def get_event_class(cls) -> Type[BaseEvent]:
        return BandUpdateEvent

    @abstractmethod
    def handle(self, message: BandUpdateMessage) -> None:
        pass
