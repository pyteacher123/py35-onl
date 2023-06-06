"""
port 80 -> HTTP
port 443 -> HTTPS

http request - client side
http response - server side


HTTP Request structure:
1) Text 
2) Message divided into 3 parts: 
        Part 1: <method name> <url_path> <http_version> | GET / HTTP/1.1
        Part 2: <header_name>: <value> (repeatable) | HOST: google.com
        Part 3: <html>, <json>, <plain_text> | Hello World!

        
HTTP Response structure:
1) Text
2) Message divided into 3 parts:
        Part 1: <http_version> <status_code> | HTTP/1.1 200 OK
        Part 2: <header_name>: <value> | Content-Length: 256
        Part 3: <html>, <json>, ... | <h1>Hello World!</h1>
"""
import socket
import ssl
from urllib.parse import urlparse


def send_tcp_message(domain_name: str, message: str, port: int = 80) -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = socket.gethostbyname(domain_name)
    print("Create connection.")
    sock.connect((server_address, port))

    # Add encryption
    if port == 443:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock=sock, server_hostname=domain_name)

    print("Message sended.")
    sock.sendall(message.encode())  # message -> http request
    message: bytes = bytes()
    BUFF_SIZE = 4096
    while True:
        data = sock.recv(BUFF_SIZE)
        message += data
        if len(data) < BUFF_SIZE:
            break
    sock.close()
    return message.decode()  # http response


def get_message(method: str, url_path: str, domain_name: str) -> str:
    message = f"{method} {url_path} HTTP/1.1\nHost: {domain_name}\n\n"
    return message


def request(method: str, url: str) -> str:
    url_sections = urlparse(url=url)
    url_path = url_sections.path + "?" + url_sections.query
    domain_name = url_sections.netloc
    message = get_message(method=method, url_path=url_path, domain_name=domain_name)
    if url_sections.scheme == 'https':
        port = 443
    else:
        port = 80
    return send_tcp_message(domain_name=domain_name, message=message, port=port)


if __name__ == '__main__':
    res = request("GET", "https://www.google.com/")
    print(res)
