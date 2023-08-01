import threading
import time

import requests

import main
import main2


def send_to_public():
    while True:
        requests.post("http://192.168.0.106:5000/dictSend", json=main.dict_)
        requests.post("http://192.168.0.106:5000/dealsSend", json=main2.deals)
        time.sleep(5)

threading.Thread(target=send_to_public).start()
threading.Thread(target=main.main).start()
threading.Thread(target=main2.tracking).start()
