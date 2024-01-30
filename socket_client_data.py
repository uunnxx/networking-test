import socket


host = input('Enter host name: ')
port = int(input('Enter port number: '))

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.settimeout(10)
        if (socket_tcp.connect_ex((host, port)) == 0):
            print(
                f'Established connection to the server {host} '
                f'in the port {port}'
            )
            request = f'GET / HTTP/1.1\r\nHost:{host}\r\n\r\n'
            socket_tcp.send(request.encode())
            data = socket_tcp.recv(4096)
            print(f'Data: {repr(data)}')
            print(f'Length data: {len(data)}')
except socket.timeout as error:
    print(f'Timeout {error}')
except socket.gaierror as error:
    print(f'Connection error to the server: {error}')
except socket.error as error:
    print(f'Connection error: {error}')
