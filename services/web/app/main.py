import json

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from app.schemas import Message
from app.producer import AIOWebProducer, get_producer

app = FastAPI()


@app.post("/currency-info", response_class=JSONResponse)
async def send(message: Message, producer: AIOWebProducer = Depends(get_producer)) -> None:

    # Сначала сериализуем объект сообщения (переводим его в байты)
    message_to_produce = json.dumps(message.model_dump()).encode(encoding="utf-8")

    # Затем отправляем полученный набор байтов в назначенный топик при помощи метода
    await producer.send(value=message_to_produce)

    return JSONResponse(content={'status': 'Запрос успешно отправлен.'})
