import socket


SERVER_HOST = ('127.0.0.1', 5005)
BUFF_SIZE = 8


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    answer = input("1 - Send Message\n2 - Exit\nYour Choice: ")
    if answer == '2':
        break
    elif answer == '1':
        message = input("Enter text: ")
        sock.sendto(message.encode(), SERVER_HOST)
        response = bytes()
        while True:
            data = sock.recv(BUFF_SIZE)
            response += data
            if len(data) < BUFF_SIZE:
               break
        print(f"Response from server: {response.decode()}")

sock.close()
