# -*- coding: utf-8 -*-
#test on python 3.4 ,python of lower version  has different module organization.
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import ssl

PORT = 3997
# httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

# Handler = http.server.BaseHTTPRequestHandler
Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map={
        '.manifest': 'text/cache-manifest',
	'.html': 'text/html',
        '.png': 'image/png',
	'.jpg': 'image/jpg',
	'.svg':	'image/svg+xml',
	'.css':	'text/css',
	'.js':	'application/x-javascript',
	'': 'application/octet-stream', # Default
    }

httpd = socketserver.TCPServer(("", PORT), Handler)
# httpd.socket = ssl.wrap_socket (httpd.socket, 
#       keyfile="../cert/priv/cert/selfsigned_key.pem",
#       certfile="../cert/priv/cert/selfsigned.pem", server_side=True)
              # keyfile="path/to/key.pem", 
        # certfile='path/to/cert.pem',

print("serving at port", PORT)
httpd.serve_forever()



# httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

    #   certfile: "../cert/priv/cert/selfsigned.pem",
    #   keyfile: "../cert/priv/cert/selfsigned_key.pem"