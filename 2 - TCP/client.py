#!/usr/bin/env python

import socket
import sys

number_of_packets = 1

if len(sys.argv) > 1:
    number_of_packets = int(sys.argv[1])

TCP_IP = '10.0.0.2'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for i in range(0,number_of_packets):
    s.send(MESSAGE)
    # data = s.recv(BUFFER_SIZE)
s.close()

print "Done."