import socket

HOST = 'localhost'  # Identifica o host
PORT = 12000        # Identifica o processo na maquina


while True:
    # Instancia socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Estabelece conexao
    sock.connect((HOST, PORT))

    # Aguarda input do usuário
    message = input('Input lowercase sentence:')

    # Envia mensagem
    sock.send(message.encode())

    # Aguarda resposta
    msg_bytes = sock.recv(2048)

    print(msg_bytes.decode())

    sock.close()