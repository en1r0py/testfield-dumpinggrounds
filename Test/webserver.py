from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

httpd = HTTPServer(('localhost', 8080), CGIHTTPRequestHandler)
httpd.serve_forever()
