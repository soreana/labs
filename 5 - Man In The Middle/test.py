
from scapy.all import *
from netfilterqueue import NetfilterQueue
import codecs
import binascii



similar="$" #Search for common bytes in the packets
newData = "00$" #Insert new Data

def modify(packet):
    pkt = packet.get_payload()
    pktInfo = IP(pkt)
    pktHex = binascii.hexlify(pkt)
    print pktHex
    print pkt

    #Filter out the packets if they are TCP Protocol and going to destination port 7777. 
    #The iptable command should already be filtering by destination port 7777
    if pktInfo.haslayer(TCP) and similar in pktHex: #and pktInfo.getlayer(TCP).dport == 7777 
        pktDefault = pktHex[:104]
        pktEdit = pktHex[104:]

        pktSave = pktEdit[16:]
        pktSave = newData + pktSave
        pktNew = pktDefault + pktSave

        pktBack = bytes.fromhex(pktNew) # Convert back from hex
        pktBack = IP(pktBack) 
        del pktBack[IP].chksum   #After deleting scapy will automatically recalculate the IP and TCP Checksum
        del pktBack[TCP].chksum
        packet.set_payload(bytes(pktBack)) #Set the payload and send the packet
        print("Payload sent!")
    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(0, modify)  #Bind to Queue 0 and intercept traffic passing through queue 0
try:
    print ("[*] waiting for data")
    nfqueue.run()
except KeyboardInterrupt:
    pass

nfqueue.unbind()