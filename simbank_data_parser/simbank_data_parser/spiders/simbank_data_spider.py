import itertools
from typing import List, Any, Iterable

import scrapy
import re
from scrapy.http import Request, Response
from w3lib.http import basic_auth_header


class SimbankDataSpider(scrapy.Spider):
    """Паук для сбора данных с симбанков."""
    name: str = 'simbank_data'
    start_urls: List[str] = []
    logins_passwords: List[tuple[str]] = []

    def start_requests(self) -> Iterable[Request]:
        login_password_cycle = itertools.cycle(self.logins_passwords)
        for url in self.start_urls:
            lp = next(login_password_cycle)
            auth = basic_auth_header(lp[0], lp[1])
            try:
                yield scrapy.Request(
                    url,
                    callback=self.parse,
                    headers={'Authorization': auth},
                )
            except:
                print(f'Не удалось выполнить запрос к {url}')

    def parse(self, response: Response, **kwargs: Any) -> Any:
        try:
            regular_result_for_ip = re.sub(r"[^\d.]", "", response.url)
            for number in range(1, 129):
                yield {
                    'IP': regular_result_for_ip[:-1],
                    'SLOT': number,
                    'ICCID': response.css(f's{number}_iccid::text').get(),
                    'STATUS': response.css(f's{number}_status::text').get(),
                    'GSM': response.css(f's{number}_gsm::text').get(),
                }
        except:
            print(f'Не удалось спарсить данные с {response.url}')
