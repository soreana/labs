
import sys
import requests

def post_form(url, amount, password):
    r = requests.post(url, data = {'transfer':amount,'password':password})
    print(r.text)

if __name__ == "__main__":
    #sys.argv = ["transfer.py", "localhost", "1,000$","1234"]
    if len(sys.argv) != 4:
        print( 'Missed argument.\n usage:`python transfer.py <ip_address> <amount> <password>`')
        sys.exit(-1)
    url = 'http://' + sys.argv[1] + '/'
    post_form(url, sys.argv[2], sys.argv[3])