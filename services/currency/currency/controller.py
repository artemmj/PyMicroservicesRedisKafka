from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess
from currency.currency import settings
from currency.currency.spiders.currency_v1 import CurrencyV1Spider
from redis import asyncio as aioredis
import json


class CurrencyController(object):

    def update_redis_cache(self) -> None:

        def _crawl_currency(queue: Queue) -> None:
            try:
                process = CrawlerProcess()
                process.crawl(CurrencyV1Spider)
                process.start()
                queue.put(None)
            except Exception as exc:
                queue.put(exc)

        queue = Queue()
        process = Process(target=_crawl_currency, args=(queue,))
        process.start()
        none_or_exception = queue.get()
        process.join()
        if none_or_exception is not None:
            raise none_or_exception


    async def get_currency_info(self, currency_char_code: str) -> dict:

        async def get_currency_from_redis(char_code: str) -> dict | None:
            async with aioredis.from_url(settings.REDIS_URL) as redis_client:
                if currency_info := await redis_client.get(name=char_code):
                    return json.loads(currency_info)

        if currency_info := await get_currency_from_redis(currency_char_code):
            return currency_info
        self.update_redis_cache()
        return await get_currency_from_redis(currency_char_code)
