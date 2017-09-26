import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

stop = True
indexes = list()


class RequestHandler(BaseHTTPRequestHandler):
    global indexes

    def do_GET(self):
        indexes.append(int(self.path[1:]))
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")

class http_server(threading.Thread):
    global stop
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        port = 8888
        server = HTTPServer(('', port), RequestHandler)
        print('Listening on localhost:%s' % port)
        while(stop):
            print("adentro")
            server.handle_request()


def get_indexes():
    return indexes
