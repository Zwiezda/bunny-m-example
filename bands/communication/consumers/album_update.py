from abc import ABC, abstractmethod
from typing import Type

from bunny_m import BaseEvent, BaseConsumer

from bands.communication.events.album_update import AlbumUpdateEvent
from bands.communication.messages.album_update import AlbumUpdateMessage


class AlbumUpdateBaseConsumer(BaseConsumer, ABC):
    @classmethod
    def get_event_class(cls) -> Type[BaseEvent]:
        return AlbumUpdateEvent

    @abstractmethod
    def handle(self, message: AlbumUpdateMessage) -> None:
        pass
