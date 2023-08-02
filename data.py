import json
import threading
import time

import requests

import main


def send_to_public():
    while True:
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        requests.post("http://127.0.0.1:5000/dictSend", data=json.dumps(main.dict_), headers=headers)
        time.sleep(5)

threading.Thread(target=send_to_public).start()
threading.Thread(target=main.main).start()
