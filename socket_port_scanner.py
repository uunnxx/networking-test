import socket
import sys
from datetime import datetime
import errno


remote_server = input('Enter a remote host to scan: ')
remote_server_ip = socket.gethostbyname(remote_server)
print('Please enter the range oof ports you would like to scan on the machine')

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f'Please wait, scanning remote host {remote_server_ip}')

time_init = datetime.now()

try:
    for port in range(start_port, end_port):
        print(f'Checkcing port {port}...')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((remote_server_ip, port))
        if result == 0:
            print(f'Port {port}:\tOpen')
        else:
            print(f'Port {port}:\tClosed')
            print(f'Reason: {errno.errorcode[result]}')
        sock.close()
except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print('Could not connect to server')
    sys.exit()

time_finish = datetime.now()
total = time_finish - time_init

print(f'Port Scanning Completed in: {total}')
