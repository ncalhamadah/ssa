#!/usr/bin/env python3
import socket
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8753         # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #used to connect to a server that is listening on the host (IP address or hostname) and port that are specified.
    #HOST - address of the remote server to connect, could be IP or DNS. In this case its using my loopback address
    #PORT - the port where the server is listening for incoming connections
    #
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))