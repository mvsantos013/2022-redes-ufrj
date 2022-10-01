import socket

PORT = 12000 # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o endereço e porta
sock.bind(('', PORT))

# Colar em modo de espera
print(f'Listening at port {PORT}.')
sock.listen(1) # Quantidade de conexoes pendentes

while True:
    # Aceita conexão
    client_sock, address = sock.accept()

    print(f'connected to {address}')

    # Aguarda mensagem
    msg_bytes = client_sock.recv(2048)

    message = msg_bytes.decode().upper()

    # Envia mensagem
    client_sock.send(message.encode())

    client_sock.close()