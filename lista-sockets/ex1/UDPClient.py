import socket

HOST = 'localhost'  # Identifica o host
PORT = 12000        # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Aguarda input do usuário
    message = input('Input lowercase sentence:')

    # Permite usuário encerrar aplicação
    if(message == 'exit'):
        sock.close()
        break

    # Envia mensagem
    sock.sendto(message.encode(), (HOST, PORT))

    # Aguarda resposta
    msg_bytes, server_address = sock.recvfrom(2048)

    print(msg_bytes.decode())