import socket

HOST = 'localhost'  # Identifica o host
PORT = 12000        # Identifica o processo na maquina

user_is_connected = False

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece conexao
sock.connect((HOST, PORT))

while True:
    # Aguarda input do usuário
    if(user_is_connected):
        message = input('You are connected. Send any message to receive the secret data: ')
    else:
        message = input('User and password separated by ";": ')

    # Envia mensagem
    sock.send(message.encode())

    # Aguarda resposta
    msg_bytes = sock.recv(2048)

    message = msg_bytes.decode()

    if(message == 'login successful.'):
        user_is_connected = True

    print(message)