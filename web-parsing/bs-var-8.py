# 8. Напишіть Python-програму для отримання з веб-сторінки усіх URL-адрес, які розміщуються в тезі <li>.
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from pip._vendor import requests

try:
    html = urlopen('https://www.python.org/')
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("Ready to work")

bs = BeautifulSoup(html.read(), 'html.parser')

# for a in bs.find_all('li'):
#   r = a.find('a')
#   print(r.attrs['href'])

resp = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
currency_data = resp.json()


class Converter:
    def __init__(self, UAHAmount = 1000, USDAmount=100, EURAmount = 100, RURAmount = 5000, BTCAmount = 5):
        self.__UAHAmount = UAHAmount
        self.__USDAmount = USDAmount
        self.__EURAmount = EURAmount
        self.__RURAmount = RURAmount
        self.__BTCAmount = BTCAmount

    @property
    def UAHAmount(self):
        return self.__UAHAmount

    @property
    def USDAmount(self):
        return self.__UAHAmount

    @property
    def EURAmount(self):
        return self.__EURAmount

    @property
    def RURAmount(self):
        return self.__RURAmount

    @property
    def BTCAmount(self):
        return self.__BTCAmount

    def buy(self): return 0

    def sell(self): return 0

    buy_USD = [data['buy'] for data in currency_data if data['ccy'] == 'USD']
    sell_USD = [data['sale'] for data in currency_data if data['ccy'] == 'USD']
    USD = [float(buy_USD[0]), float(sell_USD[0])]

    buy_EUR = [data['buy'] for data in currency_data if data['ccy'] == 'EUR']
    sell_EUR = [data['sale'] for data in currency_data if data['ccy'] == 'EUR']
    EUR = [float(buy_EUR[0]), float(sell_EUR[0])]

    buy_RUR = [data['buy'] for data in currency_data if data['ccy'] == 'RUR']
    sell_RUR = [data['sale'] for data in currency_data if data['ccy'] == 'RUR']
    RUR = [float(buy_RUR[0]), float(sell_RUR[0])]

    buy_BTC = [data['buy'] for data in currency_data if data['ccy'] == 'BTC']
    sell_BTC = [data['sale'] for data in currency_data if data['ccy'] == 'BTC']
    BTC = [float(buy_BTC[0]), float(sell_BTC[0])]


class ConvertUSD(Converter):
    def buy(self):
        return f"{self.UAHAmount / self.USD[0]} usd"

    def sell(self):
        return f"{self.USDAmount * self.USD[1]} grn"


class ConvertEUR(Converter):
    def buy(self):
        return f"{self.UAHAmount / self.EUR[0]} eur"

    def sell(self):
        return f"{self.EURAmount * self.EUR[1]} grn"


class ConvertRUR(Converter):
    def buy(self):
        return f"{self.UAHAmount / self.RUR[0]} rur"

    def sell(self):
        return f"{self.RURAmount * self.RUR[1]} grn"


class ConvertBTC(Converter):
    def buy(self):
        return f"{self.UAHAmount / self.BTC[0] * self.USD[0]} btc"

    def sell(self):
        return f"{self.BTCAmount * self.BTC[1] * self.USD[1]} grn"


test = ConvertBTC()
print(test.buy())