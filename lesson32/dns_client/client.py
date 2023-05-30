import socket
import random
import binascii
import dnslib
from dataclasses import dataclass


@dataclass
class DNSConfig:
    server_address: str
    port: int


@dataclass
class DNSMessageHeader:
    ID: str = "{:04x}".format(random.choice(range(65536)))  # 0 ... 65535
    QR: str = '0'
    OPCODE: str = '0'.zfill(4)
    AA: str = '0'
    TC: str = '0'
    RD: str = '1'
    RA: str = '0'
    Z: str = '0'.zfill(3)
    RCODE: str = '0'.zfill(4)
    QDCOUNT: str = "{:04x}".format(1)
    ANSCOUNT: str = "{:04x}".format(0)
    NSCOUNT: str = "{:04x}".format(0)
    ARCOUNT: str = "{:04x}".format(0)

    def __str__(self) -> str:
        return self.ID + self._get_flags() + self.QDCOUNT + self.ANSCOUNT + self.NSCOUNT + self.ARCOUNT
    
    def _get_flags(self) -> str:
        flags_params = self.QR + self.OPCODE + self.AA + self.TC + self.RD + self.RA + self.Z + self.RCODE
        return "{:04x}".format(int(flags_params, 2))



def get_message(domain_name: str) -> str:
    headers_section = str(DNSMessageHeader())
    buf = ''
    for part in domain_name.split('.'):
        part_len = "{:02x}".format(len(part))
        domain_part = binascii.hexlify(part.encode()).decode()
        buf += part_len + domain_part
    buf += "00"
    QNAME = buf
    QTYPE = "{:04x}".format(1)
    QCLASS = "{:04x}".format(1)
    message = headers_section + QNAME + QTYPE + QCLASS
    return message


def send_udp_request(message: str, dns_server: DNSConfig) -> bytes:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Message sent.")
    sock.sendto(binascii.unhexlify(message), (dns_server.server_address, dns_server.port))
    response = bytes()
    BUFF_SIZE = 4069
    while True:
        data = sock.recv(BUFF_SIZE)
        response += data
        if len(data) < BUFF_SIZE:
            break
    return response


if __name__ == '__main__':
    dns_conf = DNSConfig(
        server_address='8.8.8.8',
        port=53
    )
    while True:
        choice = input("1 - Get IP\n2 - Exit\nEnter: ")
        if choice == '2':
            break
        elif choice == '1':
            domain_name = input("Enter domain name: ")
            message = get_message(domain_name=domain_name)
            response = send_udp_request(message=message, dns_server=dns_conf)
            res = dnslib.DNSRecord().parse(response)
            print(res)
            try:
                ip_address = res.rr[0].rdata
            except IndexError:
                print("Bad domain name.")
                continue
            print(f"IP Address: {ip_address}")