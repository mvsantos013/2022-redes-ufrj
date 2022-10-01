import socket

HOST = 'localhost'  # Identifica o host
PORT = 12003        # Identifica o processo na maquina

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece conexao
sock.connect((HOST, PORT))

message = sock.recv(2048).decode()
print(message)

nome = input('Digite seu nome: ')

sock.send(nome.encode())

while True:
    message = sock.recv(2048).decode()
    
    print(message)
    
    if(message == '' or 'inválida' in message):
        sock.close()
        break
        

    opcao = input('Escolha uma opção: ')

    sock.send(opcao.encode())