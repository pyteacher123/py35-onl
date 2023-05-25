import socketserver


SERVER_HOST = ('127.0.0.1', 8001)


class EchoRequestHandler(socketserver.BaseRequestHandler):
    BUFF_SIZE: int = 8

    def handle(self) -> None:
        print(f"Recieved connection from {self.client_address}")
        while True:
            message = bytes()
            while True:
                data = self.request.recv(self.BUFF_SIZE)
                message += data
                if len(data) < self.BUFF_SIZE:
                   break
            if not data:
                break
            print(message.decode())
            self.request.sendall(message)


if __name__ == "__main__":
    server = socketserver.TCPServer(server_address=SERVER_HOST, RequestHandlerClass=EchoRequestHandler).serve_forever()
    print(server)
