__description__ = 'Check a target URL with multiple payloads to detect the SSRF vulnerability.'
import logging
import time
import optparse
from single_ssrf_check import check_ssrf_for_site
from webserver_thread import http_server, get_indexes, stop

def get_payloads(source):
    try:
        payloads_file_descriptor = open(source, 'rb')
    except IOError:
        logging.error('-p parameter was not provided and \'payloads.txt\' was missing.')
        raise
    payloads = payloads_file_descriptor.readlines()
    payloads_file_descriptor.close()
    return payloads


def main():
    # Parameters
    oParser = optparse.OptionParser(usage='%s\nUsage: ssrf_checker [options]' % (__description__))
    oParser.add_option('-t', '--target-url', default=None, help='Target URL.')
    oParser.add_option('-p', '--payloads', default='payloads.txt', help='File containing payloads.')
    (options, args) = oParser.parse_args()
    # Logs
    logging.basicConfig(filename='%s_%s.log' % ('log_', str(time.time())),
                        filemode='wb',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    # Input validations
    if options.target_url is None:
        raise Exception('Missing parameter: target url.')
    # Start HTTP Server to handle requests from the target page
    thread_server = http_server()
    thread_server.start()
    time.sleep(5)
    # Load payloads
    payloads = [payload.strip('\r\n ') for payload in get_payloads(options.payloads)] # Strips whitespaces, \r and \n
    logging.debug('Payload list: %s' % (str(payloads)))
    vulnerabilities = []
    index = 1
    for payload in payloads:
        vulnerabilities.extend(check_ssrf_for_site(options.target_url, payload, str(index)))
    stop()
    results = [vulnerability.to_string() for vulnerability in vulnerabilities if (vulnerability.index in get_indexes())]
    if results != []:
        for result in results:
            print(results)
            print('--------------------')
    else:
        print('No SSRF vulnerability detected.')


if __name__ == '__main__':
    main()
    # requests.post('http://httpbin.org/post', data = {'key':'value'})
