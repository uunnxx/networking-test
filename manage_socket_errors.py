import socket


host = 'domain/ip_address'
port = 80

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(mysocket)
    mysocket.settimeout(5)
except socket.error as error:
    print(f'socket create error: {error}')

try:
    mysocket.connect((host, port))
    print(mysocket)
except socket.timeout as error:
    print(f'Timeout {error}')
except socket.gaierror as error:
    print(f'Connection error to the server: {error}')
except socket.error as error:
    print(f'Connection error: {error}')
