import socket

HOST = 'localhost'  
PORT = 12000

sock = socket.socket() 
sock.connect((HOST, PORT))


while True:
    val = input('Send a message: ')

    if val == 'exit':
        break

    sock.send(val.encode())

    msg_bytes = sock.recv(1024)
    msg = msg_bytes.decode()

    print('Received:', msg)

print('Closing Connection')
sock.close()