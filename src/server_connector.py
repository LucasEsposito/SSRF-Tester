import requests
import time



def succeed_connection_from(target_url, function):
    url = 'http://127.0.0.1:8888/get_result'
    return requests.get(url).json()['vulnerable']


def send_time():
    now = str(time.time())
    url = 'http://127.0.0.1:8888/time'
    payload = {'time': now}
    requests.post(url, payload)
