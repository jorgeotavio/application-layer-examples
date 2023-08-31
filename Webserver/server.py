from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    print("Server is running in port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
