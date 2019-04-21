
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

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
        
        if "transfer" in post_data:
            if S.password is None:
                self.wfile.write("Error: You should set password".encode('utf-8'))
            elif S.password == self.extract_pass(post_data):
                self.wfile.write("Transfered {} successfully.".format(
                    self.extract_money(post_data)).encode('utf-8'))
            else :
                self.wfile.write("Error: Password is incorrect.".encode('utf-8'))
        elif "pass" in post_data:
            S.password = self.extract_pass(post_data)
            self.wfile.write("Password was set.".encode('utf-8'))
        else:
            self.wfile.write("Error: Unknown key.".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()
        
if __name__ == "__main__":
    run()