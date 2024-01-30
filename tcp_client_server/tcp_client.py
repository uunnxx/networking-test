import socket


host = '127.0.0.1'
port = 9999

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    print(f'Connected to host {str(host)} in port: {str(port)}')
    message = mysocket.recv(1024)
    print(f'Message received from the server:\n{message.decode()}')

    while True:
        message = input('Enter your message > ')
        mysocket.sendall(bytes(message.encode('utf-8')))
        if message == 'quit':
            break
except socket.error as error:
    print(f'Socket error {error}')
finally:
    mysocket.close()
