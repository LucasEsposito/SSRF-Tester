__description__ = 'Check a target URL with multiple payloads to detect the SSRF vulnerability.'
import requests
import logging
import time
import optparse
from single_ssrf_check import check_ssrf_for_site


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
    oParser = optparse.OptionParser(usage='%s\nUsage: ssrf_checker [options]' % (__description__))
    oParser.add_option('-t', '--target-url', default=None, help='Target URL.')
    oParser.add_option('-p', '--payloads', default='payloads.txt', help='File containing payloads.')
    (options, args) = oParser.parse_args()
    logging.basicConfig(filename='%s_%s.log' % (options.target_url, str(time.time())),
                        filemode='wb',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    if options.target_url is None:
        raise Exception('Missing parameter: target url.')
    payloads = [payload.strip('\r\n ') for payload in get_payloads(options.payloads)] # Strips whitespaces, \r and \n
    logging.debug('Payload list: %s' % (str(payloads)))

if __name__ == '__main__':
    main()
    # requests.post('http://httpbin.org/post', data = {'key':'value'})
