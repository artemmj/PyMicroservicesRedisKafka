from aiokafka import AIOKafkaProducer
from web.app import settings
import asyncio

event_loop = asyncio.get_event_loop()


class AIOWebProducer:
    """
    Продюсер, по сути - это специальный класс, который может
    взаимодействовать с брокером сообщений и предоставляет
    интерфейс отправки сообщения по нужному топику.
    """
    def __init__(self):
        # AIOKafkaProducer - представляет из себя интерфейс взаимодействия
        # с брокером от лица производителя (продьюсера) сообщений. В качестве
        # параметров указан текущий цикл событий и KAFKA_BOOTSTRAP_SERVERS.
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            loop=event_loop,
        )
        self.__produce_topic = settings.PRODUCE_TOPIC

    async def start(self) -> None:
        await self.__producer.start()

    async def stop(self) -> None:
        await self.__producer.stop()

    async def send(self, value: bytes) -> None:
        """
        Функция нкапсулирует создание и закрытие соединения перед отправкой сообщения
        по нужному топику. Стоит отметить, что отправляем данные мы в байтах. Это следует
        из документации пакета и устройства самой Kafka.
        """
        await self.start()
        try:
            await self.__producer.send(
                topic=self.__produce_topic,
                value=value,
            )
        finally:
            await self.stop()


def get_producer() -> AIOWebProducer:
    """Функция нужна для удобной инъекции продюсера в end-point."""
    return AIOWebProducer()
