import json

import redis
import scrapy
from scrapy import http as scraphttp

from currency.currency import settings


class CurrencyV1Spider(scrapy.Spider):
    name = "currency_v1"
    allowed_domains = ["www.cbr.ru"]
    start_urls = ["https://www.cbr.ru/scripts/xml_daily.asp"]

    def parse(self, response: scraphttp.Response):
        currencies = response.xpath("//ValCurs//Valute")
        with redis.from_url(url=settings.REDIS_URL) as redis_client:
            for currency in currencies:
                redis_client.set(
                    name=self.get_currency_redis_key(currency),
                    value=self.get_currency_redis_value(currency),
                    ex=settings.CURRENCY_REDIS_CACHE_TIME_IN_SECONDS,
                )

    @staticmethod
    def get_currency_redis_key(selector) -> str:
        return selector.xpath(".//CharCode//text()").get()

    @staticmethod
    def get_currency_redis_value(selector) -> bytes:
        return json.dumps(
            {
                "currency_value": selector.xpath(".//Value//text()").get()
            }
        ).encode("utf-8")
