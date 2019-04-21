
import sys
import requests

def post_form(url, value):
    r = requests.post(url, data = {'password':value})
    print(r.text)

if __name__ == "__main__":
    #sys.argv = ["transfer.py", "localhost", "1234"]
    if len(sys.argv) != 3:
        print( 'Missed argument.\n usage:`python set_password.py <ip_address> <password>`')
        sys.exit(-1)
    url = 'http://' + sys.argv[1] + '/'
    int(sys.argv[2])
    post_form(url, sys.argv[2])