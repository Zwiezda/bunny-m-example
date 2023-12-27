from abc import ABC, abstractmethod
from typing import Type

from bunny_m import BaseEvent, BaseConsumer

from bands.communication.events.concert_update import ConcertUpdateEvent
from bands.communication.messages.concert_update import ConcertUpdateMessage


class ConcertUpdateBaseConsumer(BaseConsumer, ABC):
    @classmethod
    def get_event_class(cls) -> Type[BaseEvent]:
        return ConcertUpdateEvent

    @abstractmethod
    def handle(self, message: ConcertUpdateMessage) -> None:
        pass
