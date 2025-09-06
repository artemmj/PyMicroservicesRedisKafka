from aiokafka import AIOKafkaProducer
from web.app import settings
import asyncio

event_loop = asyncio.get_event_loop()


class AIOWebProducer:
    """
    Этот класс, по сути, обертка, которая взаимодействует с брокером
    сообщений и предоставляет интерфейс отправки сообщения по нужному топику.
    """
    def __init__(self):
        # AIOKafkaProducer представляет из себя интерфейс взаимодействия
        # с брокером от лица производителя (продюсера) сообщений. В качестве
        # параметров указан текущий цикл событий и KAFKA_BOOTSTRAP_SERVERS.
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            loop=event_loop,
        )
        self.__produce_topic = settings.PRODUCE_TOPIC

    async def start(self) -> None:
        """Открывает соединение с кластером Kafka."""
        await self.__producer.start()

    async def stop(self) -> None:
        """Очищает все ожидающие данные и закрывает соединение."""
        await self.__producer.stop()

    async def send(self, value: bytes) -> None:
        """
        Функция инкапсулирует создание и закрытие соединения перед
        отправкой сообщения по нужному топику. Данные отправляем в байтах.
        """
        await self.start()
        try:
            await self.__producer.send(topic=self.__produce_topic, value=value)
        finally:
            await self.stop()


def get_producer() -> AIOWebProducer:
    """Функция для удобной инъекции продюсера в end-point."""
    return AIOWebProducer()
