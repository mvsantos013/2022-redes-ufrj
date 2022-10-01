import socket

HOST = 'localhost'  # Identifica o host
PORT = 12001        # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece conexao
sock.connect((HOST, PORT))



while True:
    # Aguarda input do usuário
    n = int(input('N: ')) 

    for i in range(n):
        # Envia mensagem
        print(i)
        sock.send(f'num: {i}'.encode())