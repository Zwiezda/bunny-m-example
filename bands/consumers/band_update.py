import time

from bands.communication.consumers import BandUpdateBaseConsumer
from bands.communication.messages import BandUpdateMessage


class BandUpdateConsumer(BandUpdateBaseConsumer):
    def handle(self, message: BandUpdateMessage) -> None:
        print(f"BandUpdateEventConsumer - I'am get {message.name} band")
        time.sleep(1)
