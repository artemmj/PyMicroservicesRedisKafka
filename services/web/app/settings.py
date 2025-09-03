import os


# Адрес сервера брокера (их может быть несколько)
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
# Топик, куда наш web-сервис будет отправлять сообщения. Scrapy будет этот топик слушать
PRODUCE_TOPIC = os.getenv("WEB_TOPIC")
