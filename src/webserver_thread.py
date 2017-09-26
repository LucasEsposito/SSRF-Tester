import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser


class RequestHandler(BaseHTTPRequestHandler):
    global output_path
    def do_GET(self):
        
        request_path = self.path
        output_path.append(request_path)        
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        
    def do_POST(self):
        request_path = self.path
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        self.send_response(200)
    
    do_PUT = do_POST
    do_DELETE = do_GET

class http_server(threading.Thread):
	global stop
	global server

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		print('Listening on localhost:%s' % port)
		while(stop):
			print("adentro")
			server.handle_request()

stop = True
port = 8888
output_path = []
server = HTTPServer(('', port), RequestHandler)

thread_server = http_server()

thread_server.start()


while(1):
	time.sleep(1)
	print("dentro del main")
	print(output_path)
	stop = False
	break

print("Estoy en main")
