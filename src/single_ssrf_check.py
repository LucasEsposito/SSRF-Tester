import requests
import logging
import server_connector

functions = [requests.get, requests.head, requests.options, requests.post, requests.put]


def request_function_to_string(function):
    return str(function).split(' ')[1].upper()


class SSRFVulnerability:

    def __init__(self, target_url, payload, function):
        self.target_url = target_url
        self.payload = payload
        self.function = request_function_to_string(function)


def is_vulnerable(target_url, payload, function):
    # TODO: Validate connection exceptions
    response = function(target_url + payload)
    return response.ok and server_connector.succeed_connection_from(target_url, request_function_to_string(function))


def check_ssrf_for_site(target_url, payload):
    vulnerabilities = []
    # Get, Head, Options, Put, Post
    for function in functions:
        if is_vulnerable(target_url, payload, function):
            vulnerabilities.append(SSRFVulnerability(target_url, payload, function))
    return vulnerabilities


def asdadsadasdsada():
    response = function(url) if payload is None else function(url, payload)
    requests.post('http://httpbin.org/post', data={'key': 'value'})
