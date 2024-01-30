import socket


try:
    hostname = socket.gethostname()
    print(f'gethostname: {hostname}')
    ip_address = socket.gethostbyname(hostname)
    print(f'Local IP address: {ip_address}')
    print(f'gethostbyname: {socket.gethostbyname("www.python.org")}')
    print(f'gethostbyname_ex: {socket.gethostbyname_ex("www.python.org")}')
    print(f'gethostbyaddr: {socket.gethostbyaddr("8.8.8.8")}')
    print(f'getaddrinfo: {socket.getaddrinfo("www.google.com", None, 0, socket.SOCK_STREAM)}')
except socket.error as error:
    print(str(error))
    print('Connection error')
