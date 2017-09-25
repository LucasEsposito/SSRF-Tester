import requests
import time


def succeed_connection_from(target_url, function):
    url = '127.0.0.1:5050/get_result'
    return requests.get(url).json()['vulnerable']


def send_time():
    now = str(time.time())
    url = '127.0.0.1:5050/time'
    payload = {'time': now}
    requests.post(url, payload)
