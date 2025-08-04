#!/usr/bin/env python3
import http.server
import socketserver
import os

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If accessing root, redirect to dashboard
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def list_directory(self, path):
        # Disable directory listing
        self.send_error(403, "Directory listing not allowed")
        return None

if __name__ == "__main__":
    PORT = 8000
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Server running at http://localhost:{PORT}")
        print(f"📊 Dashboard: http://localhost:{PORT}")
        print(f"🔄 Auto-refresh: http://localhost:{PORT}/index_auto.html")
        print("Press Ctrl+C to stop")
        httpd.serve_forever() 