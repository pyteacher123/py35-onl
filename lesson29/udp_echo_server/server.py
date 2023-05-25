import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 5005))

while True:
    BUFF_SIZE = 8
    message = bytes()
    while True:
        data, addr = server_socket.recvfrom(BUFF_SIZE)
        print(f"Recieved connection from {addr}")
        message += data
        if len(data) < BUFF_SIZE:
            break

    server_socket.sendto(message, addr)
