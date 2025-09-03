from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import FastAPI, Depends
from app.schemas import Message
from app.producer import get_producer
import json

if TYPE_CHECKING:
    from app.producer import AIOWebProducer

app = FastAPI()


@app.post("/currency-info")
async def send(message: Message, producer: AIOWebProducer = Depends(get_producer)) -> None:
    # Сначала сериализуем объект сообщения (переводим его в байты)
    message_to_produce = json.dumps(message.model_dump()).encode(encoding="utf-8")
    # Затем отправляем полученный набор байтов в назначенный топик при помощи метода
    await producer.send(value=message_to_produce)
