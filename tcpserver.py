# tcpserver.py
 
from socket import socket
from socket import SOL_SOCKET, SO_REUSEADDR
 
sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
 
sock.bind(('171.69.52.97', 9000))
sock.listen(15)
 
while True:
    conn, who = sock.accept()
    ip, port = who
    msg = conn.recv(1024)
 
    print 'Connection from:'
    print '  ip =', ip
    print '  port =', port
    print '  msg =', msg
