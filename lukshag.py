from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>luksha</title>
    </head>
    <body>
       <center><h2>Laptop config (25014479)</h2>
        <table border="">
        <tr>
            <th>Device name</th>
            <th>Storage></th>
            <th>Ram</th>
            <th>Processor</th>
            <th>Graphics card</th>
        </tr>
        <tr>
            <td>lenovo</td>
            <td>256 GB</td>
            <td>8GB</td>
            <td>i3</td>
            <td>64GB</td>
        </tr>
        <tr>
            <td>Acer</td>
            <td>512GB</td>
            <td>32GB</td>
            <td>i5</td>
            <td>128GB</td>
        </tr>
        <tr>
            <td>Asus</td>
            <td>1TB</td>
            <td>32GB</td>
            <td>AMD ryzan</td>
            <td>128GB</td>
        </tr>
        <tr>
            <td>Mac Book</td>
            <td>512GB</td>
            <td>32GB</td>
            <td>i5</td>
            <td>128GB</td>
        </tr>
        <tr>
            <td>Google chrome book</td>
            <td>256GB</td>
            <td>32GB</td>
            <td>i3</td>
            <td>128GB</td>
        </tr>
        </table>
        </center>
    </body>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()