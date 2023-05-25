"""
socket.socket(<Network Protocol>, <Trasport Protocol>)
Network Protocol: 
socket.AF_INET => IPv4
socket.AF_INET6 => IPv6

Transport Protocol:
socket.SOCK_STREAM => TCP
socket.SOCK_DGRAM => UDP
"""
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
print(f"Server socket created: {server_socket}")
server_socket.bind(('127.0.0.1', 5001))
server_socket.listen()

while True:
    print("Server is ready to accept connection.")
    client_socket, addr = server_socket.accept()
    print(f"Connection recieved {addr}")
    while True:
        message = bytes()
        BUFF_SIZE = 8
        while True:
            data = client_socket.recv(BUFF_SIZE)
            message += data
            if len(data) < BUFF_SIZE:
               break
        if not data:
            break
        print(message.decode())
        client_socket.sendall(message)


server_socket.close()
