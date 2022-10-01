import socket

HOST = 'localhost'  # Identifica o host
PORT = 12000        # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece conexao
sock.connect((HOST, PORT))

while True:
    # Aguarda input do usuário
    message = input('Input lowercase sentence:')

    # Permite usuário encerrar aplicação
    if(message == 'exit'):
        sock.close()
        break

    # Envia mensagem
    sock.send(message.encode())

    # Aguarda resposta
    msg_bytes = sock.recv(2048)

    print(msg_bytes.decode())