import socket

PORT = 12000 # Identifica o processo na maquina

USER = 'user'
PASSWORD = 'psw'

user_is_connected = False

SECRET_DATA = 'This is a secret message.'

# Instancia socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o endereço e porta
sock.bind(('', PORT))

# Colar em modo de espera
print(f'Listening at port {PORT}.')
sock.listen(1) 

# Aceita conexão
client_sock, address = sock.accept()

print(f'connected to {address}')

while True:
    # Aguarda mensagem
    msg_bytes = client_sock.recv(2048)

    message = msg_bytes.decode()
    
    if(not user_is_connected):
        try:
            login, password = message.split(';')
            if(login == USER and password == PASSWORD):
                user_is_connected = True
                client_sock.send('login successful.'.encode())
            else:
                raise Exception('Invalid user or password.')
        except:
            client_sock.send('login failed.'.encode())
    else:
        client_sock.send(SECRET_DATA.encode())