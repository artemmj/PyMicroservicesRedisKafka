<h1>Python Microservices (with Kafka)</h1>
<p>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/0c233ba5-f0e4-44b8-b5ef-6608867e6d3b" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/ecaae263-500a-4a80-b1ed-4296e830783c" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/3675cec5-2b17-408c-88b8-de1a7737aef2" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/c56eb267-fbac-4750-a473-deec88a84578" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/acc192cb-42af-476f-9eb9-b66fe10f9164" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/2d857681-aa69-4644-9b98-90eac1c876dd" width="50" height="50"/>
</p>
<p>Этот проект является примером микросервисной архитектуры, созданной на Python с использованием Apache Kafka 💡</p>

## Сервисы:
 - web (FASTApi)
 - notify (Aiogram)
 - currency (Scrapy)

## Как это работает?
Первый шаг - пользователь отправляет запрос в веб-службу на FASTApi с единственной точкой входа. Эта конечная точка ожидает два параметра: код валюты и идентификатор пользователя в telegram.

После этого веб-служба отправляет сообщение в службу обмена валют. Currency service - это паук, который обрабатывает информацию из этого открытого API и работает на платформе Scrapy на python.

В конце валютный сервис выдает сообщение, уведомляющее сервис о том, что это Telegram-бот, и отправляет сообщение пользователю Telegram.

## Диаграмма
![image](https://github.com/youngwishes/MSA/assets/92817776/8c0bbc2c-0a38-43be-8fa1-3486a00e7558)

# Стартуем

1. Склонировать репо

```
git clone https://github.com/youngwishes/fastapi-kafka.git
```
2. Создать файл .env и скопировать в него содержимое .env.dev
3. Вставить так же свой телеграм-токен
4. Поднимаем в докере командой
```
docker compose up -d --build
```
