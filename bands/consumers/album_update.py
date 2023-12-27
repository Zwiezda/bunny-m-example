import time

from bands.communication.consumers import AlbumUpdateBaseConsumer
from bands.communication.messages import AlbumUpdateMessage


class AlbumUpdateConsumer(AlbumUpdateBaseConsumer):
    def handle(self, message: AlbumUpdateMessage) -> None:
        print(f"AlbumUpdateEventConsumer - I'am get {message.title} album")
        time.sleep(3)
        raise Exception("Something went wrong")
