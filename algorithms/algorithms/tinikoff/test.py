import requests
import re
import logging
import time



ETHUSD = "http://www.binance.com/ru/futures/ETH_USDT"


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


def get_ethusd_price():
    r = requests.get(ETHUSD, headers={'Cache-Control': 'no-cache', "Pragma": "no-cache"})
    page = r.text
    price = float(list(re.search(r'><title data-shuvi-head="true">(\S+)', page).groups())[0])
    return price


def count_delta(num_1, num_2):
    return abs(((num_1 - num_2)/num_2)*100)


while True:
    price_1 = get_ethusd_price()
    time.sleep(3600)
    price_2 = get_ethusd_price()
    delta = count_delta(price_2, price_1)
    log.info(f"Delta = {delta}")
    if delta > 1:
        log.info(f'Стоимость изменилась на {delta}%')
