import itertools
import scrapy
import re
from scrapy.http import Request, Response
from typing import List, Any, Iterable
from w3lib.http import basic_auth_header


class ExampleSpider(scrapy.Spider):
    """Паук для сбора данных со шлюзов."""
    name = 'messages'
    start_urls: List[str] = []
    logins_passwords: List[tuple[str]] = []

    def start_requests(self) -> Iterable[Request]:
        login_password_cycle = itertools.cycle(self.logins_passwords)
        for url in self.start_urls:
            lp = next(login_password_cycle)
            auth = basic_auth_header(lp[0], lp[1])
            yield scrapy.Request(
                url,
                callback=self.handle_response,
                headers={'Authorization': auth},
            )

    def handle_response(self, response: Response, **kwargs: Any) -> Any:
        try:
            data = response.css('#tools_page_6_div > script:nth-child(4)::text').get()
            messages = re.findall(r'"([^"]*)"', data)
            yield {
                'URL': response.url,
                'MESSAGES': messages,
            }
        except:
            yield {
                'URL': response.url,
                'MESSAGES': 'Какая то ошибка парсера, ПРОВЕРИТЬ ВРУЧНУЮ!!!',
            }

