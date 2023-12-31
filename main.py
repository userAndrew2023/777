import threading
import time

import numpy as np
import requests as requests
import talib

dict_ = {}


def gett(url, crypto, interval):
    try:
        candles = requests.get(url)
        arr = np.array([float(i[4]) for i in candles.json()])
        dict_[crypto][interval] = talib.RSI(arr, 14)[-1]
    except Exception:
        pass


def price(url, crypto, interval):
    try:
        res = requests.get(url).json()
        dict_[crypto][interval] = round(float(res.get("lastPrice")), 2)
    except Exception as ee:
        print(ee)


def volume(url, crypto, interval):
    try:
        res = requests.get(url).json()
        dict_[crypto][interval] = round(float(res.get("volume")), 2)
    except Exception as ee:
        print(ee)


def change(url, crypto, interval):
    try:
        res = requests.get(url).json()
        dict_[crypto][interval] = round(float(res.get("priceChangePercent")), 2)
    except Exception as ee:
        print(ee)


def main():
    crypto = ["BTC", "ETH", "XRP", "BNB", "ADA", "DOGE", "SOL", "TRX", "MATIC", "LTC", "DOT", "AVAX",
              "WBTC", "BCH", "SHIB", "LINK", "XLM", "UNI", "ATOM", "XMR", "ETC",
              "FIL", "ICP", "LDO", "HBAR", "APT", "ARB", "NEAR", "VET", "QNT", "MKR", "GRT", "AAVE", "OP", "ALGO", "STX", "EGLD", "SAND", "EOS", "SNX", "IMX", "THETA", "XTZ", "APE"]
    for i in crypto:
        if dict_.get(i) is None:
            dict_[i + 'USDT'] = {"h1": None, "m15": None, "d1": None, "price": None, "volume": None, "percent": None}

    while True:
        for i in crypto:
            threading.Thread(target=gett,
                             args=[f"https://api.binance.com/api/v3/klines?symbol={i + 'USDT'}&interval=1h", i + "USDT",
                                   "h1"]).start()
            threading.Thread(target=gett,
                             args=[f"https://api.binance.com/api/v3/klines?symbol={i + 'USDT'}&interval=15m",
                                   i + "USDT", "m15"]).start()
            threading.Thread(target=gett,
                             args=[f"https://api.binance.com/api/v3/klines?symbol={i + 'USDT'}&interval=1d", i + "USDT",
                                   "d1"]).start()
            threading.Thread(target=price,
                             args=[f"https://api.binance.com/api/v3/ticker?symbol={i + 'USDT'}", i + "USDT",
                                   "price"]).start()
            threading.Thread(target=volume,
                             args=[f"https://api.binance.com/api/v3/ticker?symbol={i + 'USDT'}", i + "USDT",
                                   "volume"]).start()
            threading.Thread(target=change,
                             args=[f"https://api.binance.com/api/v3/ticker?symbol={i + 'USDT'}", i + "USDT",
                                   "percent"]).start()
        print("---------------------------")
        time.sleep(30)
