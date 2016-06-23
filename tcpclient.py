# tcpclient.py
 
from socket import socket
 
sock = socket()
sock.connect(('171.69.52.97', 9000))
sock.send('Python Class was awesome!')
