import requests
import re
import logging
import time


'''
Для расчета движения цены фьючерса ETHUSDT исключая из них движения вызванные влиянием цены BTCUSDT беретса разница цены между BTCUSDT и ETHUSDT.
Аргументированно объяснить, почему я так решил сделать к сожелению я не могу.
Для получения актуальной стоимости каждые 60 минут берутся данные с сайта www.binance.com. 
После каждого расчета выводится текущая разница между текущим значением и значением которое было 60 минут назад (для истории).
При изменении цены на 1% за последние 60 минут, программа выводит сообщение в консоль "Стоимость изменилась на (число)%." 
Программа продолжает работать дальше, постоянно считывая актуальную цену и проверяя разницы каждые 60 минут.
'''


ETHUSDT = "http://www.binance.com/ru/futures/ETH_USDT"
BTCUSDT = "http://www.binance.com/ru/futures/BTCUSDT"


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


def get_price(link):
    r = requests.get(link, headers={'Cache-Control': 'no-cache', "Pragma": "no-cache"})
    page = r.text
    price = float(list(re.search(r'><title data-shuvi-head="true">(\S+)', page).groups())[0])
    return price


def count_delta(num_1, num_2):
    return abs(((num_1 - num_2)/num_2)*100)


def price_eth_without_btc():
    price = get_price(BTCUSDT) - get_price(ETHUSDT)
    return price


while True:
    price_1 = price_eth_without_btc()
    time.sleep(36)
    price_2 = price_eth_without_btc()
    delta = count_delta(price_2, price_1)
    log.info(f"Delta = {delta}")
    if delta > 1:
        log.info(f'Стоимость изменилась на {delta}%')
