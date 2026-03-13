from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        script = """@echo off
color 3
echo sup bro
pause
curl ascii.live/forrest
"""

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(script.encode())

server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"Server running on port {PORT}")
server.serve_forever()
