import requests
import logging
import time
__description__ == 'Check a target URL with multiple payloads to detect the SSRF vulnerability.'


def get_payloads(source):
    payloads_file_descriptor = open(source, 'rb')
    payloads = payloads_file_descriptor.readlines()
    payloads_file_descriptor.close()
    return payloads


def main():
    oParser = optparse.OptionParser(usage='usage: %prog [options] file\n' + __description__)
    oParser.add_option('-t', '--target-url', default=None, help='Target URL.')
    oParser.add_option('-p', '--payloads', default='payloads.txt', help='File containing payloads.')
    (options, args) = oParser.parse_args()
    logging.basicConfig(filename=options.input + '_' + str(time.time()) + '.log',
                        filemode='wb',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    payloads = get_payloads(options.payloads)

if __name__ == '__main__':
    main()
    # requests.post('http://httpbin.org/post', data = {'key':'value'})
