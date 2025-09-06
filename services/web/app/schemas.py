from pydantic import BaseModel


class Message(BaseModel):
    """Модель описывает, что ждем на вход POST запроса."""
    currency_char_code: str
    telegram_id: int
