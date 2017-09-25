import requests
import time


def succeed_connection_from(target_url, function):
    return True # TODO ask the server about the result.


def send_time():
    now = str(time.time())
    url = '127.0.0.1:5050/time'
    payload = {'time': now}
    requests.post(url, payload)
    