from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/connect':
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": False, "reason": "Not Found"}).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)

        game = params.get('game', [''])[0]
        user_key = params.get('user_key', [''])[0]
        serial = params.get('serial', [''])[0]

        if user_key == "r" and game == "ROG PRO":
            response = {
                "status": True,
                "message": "تم التحقق بنجاح"
            }
        else:
            response = {
                "status": False,
                "reason": "USER KEY OR GAME NOT REGISTERED"
            }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
