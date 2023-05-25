import socket


SERVER_HOST = ('127.0.0.1', 5002)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER_HOST)
while True:
    answer = input("1 - Send Message\n2 - Exit\nYour Choice: ")
    if answer == '2':
        break
    elif answer == '1':
        message = input("Enter text: ")
        sock.sendall(message.encode())
        response = bytes()
        BUFF_SIZE = 8
        while True:
            data = sock.recv(BUFF_SIZE)
            response += data
            if len(data) < BUFF_SIZE:
               break
        print(f"Response from server: {response.decode()}")

sock.close()
