import requests
from requests import Session
from time import time


def send_requests_separate_tcp_sessions(url: str) -> None:
    start = time()

    resp = requests.request("GET", url=url)
    print(resp.json())
    resp = requests.request("GET", url=url)
    print(resp.json())
    resp = requests.request("GET", url=url)
    print(resp.json())
    resp = requests.request("GET", url=url)
    print(resp.json())
    resp = requests.request("GET", url=url)
    print(resp.json())

    end = time()
    print(f"Execution time: {end - start} sec.")


def send_requests_one_tcp_sessions(url: str) -> None:
    start = time()

    with Session() as session:
        resp = session.request("GET", url=url)
        print(resp.json())
        resp = session.request("GET", url=url)
        print(resp.json())
        resp = session.request("GET", url=url)
        print(resp.json())
        resp = session.request("GET", url=url)
        print(resp.json())
        resp = session.request("GET", url=url)
        print(resp.json())

    end = time()
    print(f"Execution time: {end - start} sec.")

if __name__ == "__main__":
    send_requests_one_tcp_sessions("https://baconipsum.com/api/?type=meat-and-filler")
