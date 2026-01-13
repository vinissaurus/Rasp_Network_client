import http.server
import socketserver

# Server configuration
PORT = 8000  # Port the server will listen on
DIRECTORY = "."

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler serving files from the specified directory."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    """Initialize and start the HTTP server."""
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        print(f"Serving files from directory: {DIRECTORY}")
        print(f"Access it at: http://<raspberry-pi-ip>:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.shutdown()

if __name__ == "__main__":
    run_server()