import socket


SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(5)

print(f'[*] Server Listening {SERVER_IP}:{SERVER_PORT}')

client, addr = server.accept()
client.send('I am the server accepting connections on port 9999...'.encode())

print(f'[*] Accepted connection from: {addr[0]}:{addr[1]}')

while True:
    request = client.recv(1024).decode()
    print(f'[*] Received request: {request}')
    if request.lower() != 'quit':
        client.send(bytes('ACK', 'utf-8'))
    else:
        break

client.close()
server.close()
