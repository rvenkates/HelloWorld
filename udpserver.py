# udpserver.py
 
from socket import socket, AF_INET, SOCK_DGRAM
 
conn = socket(AF_INET, SOCK_DGRAM)
conn.bind(('171.69.52.97', 9000))
 
while True:
    msg, who = conn.recvfrom(1024)
    print 'Connection from: ', who
    print 'Message is: ', msg
    print
