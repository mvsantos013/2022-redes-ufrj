import time
import socket

PORT = 12000 # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o endereço e porta
sock.bind(('', PORT))

print('The server is ready to receive. (UDP)')

while True:
    # Aguarda mensagem
    t0 = time.time()
    msg_bytes, client_address = sock.recvfrom(2048)
    t1 = time.time()

    num = msg_bytes.decode()
    
    print(num, '; time elapsed:', '{0:.10f}'.format(t1 - t0))