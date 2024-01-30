import socket


def find_services_name():
    for port in [21, 22, 23, 25, 80]:
        print(f"Port <tcp>: {port} => service name: {socket.getservbyport(port, 'tcp')}")
        print(f"Port <udp>: {53} => service name: {socket.getservbyport(53, 'udp')}")


if __name__ == '__main__':
    find_services_name()
