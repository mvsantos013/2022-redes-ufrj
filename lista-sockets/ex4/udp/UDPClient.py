import socket

HOST = 'localhost'  # Identifica o host
PORT = 12000        # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Aguarda input do usuário
    n = int(input('N: '))
        
    for i in range(n):
        # Envia mensagem
        sock.sendto(f'num: {i}'.encode(), (HOST, PORT))