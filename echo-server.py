#!/usr/bin/env python3
import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8753       # Port to listen on (non-privileged ports are > 1023)

'''with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    #s.bind comes from socket library imported, using bind indicates which network interface it will use, in this case 127.0.0.1 a loopback address and port 8753, it will use it as a host waiting for client-side that matches the connection to receive data.
    # in real life scenario, I assume this should be a public domain DNS name instead of IP address, so that the client application communicates with the DNS regardless and bints to what IP is set to the domain name server.
    # i guess to secure this, it requires to implement TLS, like a certificate stored in the client-side local path to wrap the connection with a private key? Im not sure at this part. To secure data exchange between client and server, the client side must also have the certificate
    # to perform the handshake that both server-side and client-side certificates are valid. If it failes to validate, the connection wont be established?
    # summary of the code, when it the s.accept waits for a client to connect and accepts it, 'conn' represents the specific connection details socket, once it accepts it, it will print 'addr' which IP address of the connected user.
    # while connection is established (While True), data variable stored 1024 bytes from the client which is hello world from client, then conn.sendall(data) sending the data variable back to the existing 'conn' whicch is the client.
    # overall, it just waits for a client to connect and sendback data, if its already sent back and reloops and nothing is stored in data, it breaks the application, meaning ends the communication with the client
    #but in this case, it also closes the server, in real life scenario it should be back to listening, to accept multiple clients.

    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:  # Main loop to keep accepting new connections
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:  # Inner loop to handle communication with one client
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            print('Connection with', addr, 'closed')
