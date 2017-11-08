#!/usr/bin/env python3

import textwrap

from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Test app</title>
            </head>
            <body>
                <h1>webapp</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 3000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
