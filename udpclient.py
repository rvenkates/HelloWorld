# udpclient.py
 
from socket import socket, AF_INET, SOCK_DGRAM
 
conn = socket(AF_INET, SOCK_DGRAM)
conn.sendto('hello!', ('171.69.52.97', 9000))

