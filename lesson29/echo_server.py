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
print(f"Server socket created: {server_socket}")
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

while True:
    print("Server is ready to accept connection.")
    client_socket, addr = server_socket.accept()
    print(f"Connection recieved {addr}")
    message = bytes()
    BUFF_SIZE = 8
    while True:
        data = client_socket.recv(BUFF_SIZE)
        message += data
        if len(data) < BUFF_SIZE:
            break
    print(message)
    client_socket.sendall(message)
