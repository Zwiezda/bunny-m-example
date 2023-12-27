import datetime
from time import sleep

from django.core.management import BaseCommand

from bunny_m.services import ProducerManager

from bands.communication.events import BandUpdateEvent, AlbumUpdateEvent, ConcertUpdateEvent
from bands.communication.messages import BandUpdateMessage, AlbumUpdateMessage, ConcertUpdateMessage

BANDS = {
    'tatu': BandUpdateMessage(name='T.a.t.U', email='tatu@yandex.ru', site='http://www.tatu.ru'),
    'ozone': BandUpdateMessage(name='O-Zone', email='ozone@gmail.com', site='http://www.ozone.com'),
    'ramstein': BandUpdateMessage(name='Ramstein', email='ramstein@gmail.com', site='http://www.ramstein.com'),
    'sash': BandUpdateMessage(name='Sash!', email='djsash@gmail.com', site='http://www.djsash.com'),
    'indila': BandUpdateMessage(name='Indila', email='indila@gmail.fr', site='http://www.indila.fr')
}

ALBUMS = {
    'tatu': AlbumUpdateMessage(title='200 km/h in the Wrong Lane', release_date=datetime.date(2002, 1, 1), artist=BANDS['tatu']),
    'ozone': AlbumUpdateMessage(title='DiscO-Zone', release_date=datetime.date(2004, 2, 2), artist=BANDS['ozone']),
    'ramstein': AlbumUpdateMessage(title='Mutter', release_date=datetime.date(2001, 2, 2), artist=BANDS['ramstein']),
    'sash': AlbumUpdateMessage(title='Life Goes On', release_date=datetime.date(1998, 2, 2), artist=BANDS['sash']),
    'indila': AlbumUpdateMessage(title='Mini World', release_date=datetime.date(2014, 2, 2), artist=BANDS['indila']),
}

CONCERTS = {
    'tatu': ConcertUpdateMessage(location='Moscow', date=datetime.date(2002, 2, 2), artist=BANDS['tatu']),
    'ozone': ConcertUpdateMessage(location='Bucharest', date=datetime.date(2005, 2, 2), artist=BANDS['ozone']),
    'ramstein': ConcertUpdateMessage(location='Berlin', date=datetime.date(2004, 2, 2), artist=BANDS['ramstein']),
    'sash': ConcertUpdateMessage(location='Prague', date=datetime.date(1998, 2, 2), artist=BANDS['sash']),
    'indila': ConcertUpdateMessage(location='Paris', date=datetime.date(2015, 2, 2), artist=BANDS['indila']),
}


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:  # pragma: no cover
        bands_producer = ProducerManager(BandUpdateEvent)
        bands_producer.init()
        band_message = BandUpdateMessage(name='T.a.t.U', email='tatu@yandex.ru', site='http://www.tatu.ru')
        bands_producer.produce(band_message)
        bands_producer.close()

        album_producer = ProducerManager(AlbumUpdateEvent)
        concert_producer = ProducerManager(ConcertUpdateEvent)
        try:
            bands_producer.init()
            album_producer.init()
            concert_producer.init()
            while True:
                for key in BANDS.keys():
                    bands_producer.produce(BANDS[key])
                    album_producer.produce(ALBUMS[key])
                    concert_producer.produce(CONCERTS[key])
                    sleep(1)
        finally:
            bands_producer.close()
            album_producer.close()
            concert_producer.close()
