#!/usr/bin/env python3


# ref: https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class HackeriotServer(BaseHTTPRequestHandler):
    def respond_http_get(self, message):
        # ADD HTTP CODE HERE
        self.send_response(?????)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write('\nBye bye <3'.encode('utf-8'))

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self.respond_http_get('Yay! server is running :))))')


def start_server(server_class=HTTPServer, handler_class=HackeriotServer, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    start_server()
