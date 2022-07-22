#!/usr/bin/env python3


# ref: https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

from bot_analysis import test_headers


class HackeriotServer(BaseHTTPRequestHandler):
    def redirect_client(self, redirect_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'):
        self.send_response(302)
        self.send_header('Location', redirect_url)
        self.end_headers()

    def respond_http_get(self, message):
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write('\nBye bye <3'.encode('utf-8'))

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        is_legit = test_headers(self)

        if is_legit:
            self.respond_http_get('Welcome human!')
        else:
            self.respond_http_get('There\'s a snake in my boot!')

    def parse_headers(self):
        """
        build parsed headers from request
        :return: headers prepared for fingerprinting stage
        # """
        #
        parsed_headers = {
            'client_ip_address': self.client_address[0],
            'command': format(self.command),
            'request_version': format(self.request_version),
        }

        for name, value in sorted(self.headers.items()):
            parsed_headers[name] = value.rstrip()

        return parsed_headers


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
