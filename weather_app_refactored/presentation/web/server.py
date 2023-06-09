from __future__ import annotations
from socketserver import TCPServer, BaseRequestHandler
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from interfaces import WeatherServiceProtocol


@dataclass
class Request:
    method: str
    version: str
    path: str
    params: dict[str, list[str]]
    headers: dict[str, str]
    body: str


@dataclass
class Response:
    status: str
    headers: dict[str, str]
    body: str
    version: str = "HTTP/1.1"


class HttpRequestHandler(BaseRequestHandler):  # Web Server: gunicorn, uwsgi, uvicorn | flask server, wsgiref
    BUFF_SIZE = 4096

    def _parse_request(self) -> Request:
        main, *headers, _, body = self.message.split('\r\n')
        method, url_path, protocol_version = main.split()
        data = urlparse(url=url_path)
        path = data.path
        query_string = data.query
        query_params = parse_qs(query_string)
        headers = dict(header.split(': ', maxsplit=1) for header in headers)
        return Request(
            method=method,
            version=protocol_version,
            path=path,
            params=query_params,
            headers=headers,
            body=body
        )
    
    def _get_response(self, response: Response) -> str:
        mes = f"{response.version} {response.status}\r\n"
        for header, value in response.headers.items():
            mes += f"{header}: {value}\r\n"
        mes += f"Content-Length: {len(response.body)}\r\n"
        mes += f"\r\n{response.body}\r\n"
        return mes

    def handle(self) -> None:
        message: bytes = bytes()
        while True:
            data = self.request.recv(self.BUFF_SIZE)
            message += data
            if len(data) < self.BUFF_SIZE:
                break
        self.message = message.decode()
        req = self._parse_request()
        
        resp = self.server._application(request=req)
        resp = self._get_response(response=resp)

        self.request.sendall(resp.encode())


class HttpServer(TCPServer):
    allow_reuse_address: bool = True
    allow_reuse_port: bool = True

    def set_app(self, application: Callable[[Request], Response]) -> None:
        self._application = application
