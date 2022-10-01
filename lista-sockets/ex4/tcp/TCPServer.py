import socket
import time

PORT = 12001 # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o endereço e porta
sock.bind(('', PORT))

# Colar em modo de espera
print('The server is ready to receive. (TCP)')
sock.listen(1)

# Aceita conexão
client_sock, address = sock.accept()

print(f'connected to {address}')

while True:
    # Aguarda mensagem
    t0 = time.time()
    msg_bytes = client_sock.recv(2048)
    t1 = time.time()

    num = msg_bytes.decode()

    print(num, '; time elapsed:', '{0:.10f}'.format(t1 - t0))