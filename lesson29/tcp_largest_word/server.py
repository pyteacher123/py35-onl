import socket


def find_largest_word(message: str) -> str:
    max_word = None
    max_length = 0
    for word in message.split():
        if len(word) > max_length:
            max_word = word
            max_length = len(word)
    
    return max_word


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Server socket created: {server_socket}")
server_socket.bind(('127.0.0.1', 5002))
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
        result = find_largest_word(message=message.decode())
        client_socket.sendall(result.encode())
