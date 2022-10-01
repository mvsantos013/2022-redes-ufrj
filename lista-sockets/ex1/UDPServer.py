import socket

PORT = 12000 # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o endereço e porta
sock.bind(('', PORT))

print('The server is ready to receive')

while True:
    # Aguarda mensagem
    msg_bytes, client_address = sock.recvfrom(2048)

    message = msg_bytes.decode().upper()

    # Envia mensagem
    sock.sendto(message.encode(), client_address)