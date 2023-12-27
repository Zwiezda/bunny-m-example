import time

from bands.communication.consumers import ConcertUpdateBaseConsumer
from bands.communication.messages import ConcertUpdateMessage


class ConcertUpdateConsumer(ConcertUpdateBaseConsumer):
    def handle(self, message: ConcertUpdateMessage) -> None:
        print(f"ConcertUpdateEventConsumer - I'am get {message.location} {message.date} concert")
        time.sleep(20)
        raise Exception("Something went wrong")
