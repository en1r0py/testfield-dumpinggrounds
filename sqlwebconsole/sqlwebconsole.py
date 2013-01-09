from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

httpd = HTTPServer(('0.0.0.0',8043),CGIHTTPRequestHandler)
httpd.serve_forever()

