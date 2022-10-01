import socket

HOST = 'localhost'  
PORT = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

while True:
    val = input('Send a message: ')

    if val == 'exit':
        break

    sock.sendto(val.encode(), (HOST, PORT))

    msg_bytes, server_address = sock.recvfrom(1024)
    msg = msg_bytes.decode()

    print('Received:', msg)

print('Closing Connection')
sock.close()