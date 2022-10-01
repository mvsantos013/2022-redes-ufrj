import socket

PORT = 12003 # Identifica o processo na maquina

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

username = None
client_sock.send('Olá! Bem-vindo! Qual o seu nome?'.encode())

while True:
    # Aguarda mensagem
    msg_bytes = client_sock.recv(2048)

    message = msg_bytes.decode()
    
    if(message == ''):
        sock.close()
        break
    
    # Guarda nome do usuário
    if(username is None):
        username = message
        msg = f'Certo, {username}! Como posso te ajudar? Digite o número que corresponde à opção desejada:\n'
        msg += '1 - Agendar um horário de monitoria.\n'
        msg += '2 - Listar as próximas atividades da disciplina.\n'
        msg += '3 - E-mail do professor.\n'
        client_sock.send(msg.encode())
        continue
    
    if(message == '1'):
        client_sock.send('Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br.'.encode())
    elif(message == '2'):
        client_sock.send('Fique atento para as datas das próximas atividades. Confira o que vem por aí!\n\nP1: 26 de maio de 2022\nLista 3: 29 de maio de 2022'.encode())
    elif(message == '3'):
        client_sock.send('Quer falar com o professor? O e-mail dele é sadoc@dcc.ufrj.br.'.encode())
    else:
        client_sock.send('Opção inválida! Até mais.'.encode())
        sock.close()
        break