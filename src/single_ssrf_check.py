import requests
import logging

functions = [requests.get] #, requests.head, requests.post, requests.put, requests.options]


def request_function_to_string(function):
    return str(function).split(' ')[1].upper()


class SSRFVulnerability:

    def __init__(self, target_url, payload, index, function):
        self.target_url = target_url
        self.payload = payload
        self.index = index
        self.function = request_function_to_string(function)


def check_ssrf_for_site(target_url, payload, index):
    vulnerabilities = []
    for function in functions:
        function(target_url + payload.replace('<index>',index))
        vulnerabilities.append(SSRFVulnerability(target_url, payload.replace('<index>',''), index, function))
    return vulnerabilities
