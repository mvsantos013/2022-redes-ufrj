import sys
import socket
import select
import multiprocessing

HOST = ''  
PORT = 12000

class Server():
    def run(self):
        ''' Starts server. '''
        print('Starting server...')
        print('Available commands:')
        print('  - server exit [--force]\n  - server connections\n  - server help')

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.bind((HOST, PORT))
        self.sock.listen(5)
        self.sock.setblocking(False)
        
        self.inputs = [self.sock, sys.stdin]
        self.connections = {}
        self.clients = []

        print('Server is now online.')
        print(f'Listening at port {PORT}')

        while True:
            r, w, e = select.select(self.inputs, [], [])
            for ready in r:
                if ready == self.sock:
                    sock, address = self.sock.accept()
                    self.connections[sock] = address
                    print(f'New connection at {address}')
                    client = multiprocessing.Process(target=self.process_request, args=(sock, address))
                    client.start()
                    self.clients.append(client)

                elif ready == sys.stdin: 
                    cmd = input()
                    if cmd == 'server exit':
                        if self.hasConnections():
                            print(f'Server has active {len(self.connections)} connections.')
                            print('Waiting for active clients to close connection...')
                        for c in self.clients:
                            c.join()
                        self.exit()
                        return
                    elif cmd == 'server exit --force': 
                        for c in self.clients:
                            c.terminate()
                        self.exit()
                        return
                    elif cmd == 'server connections':
                        print('Connections:')
                        print(str(self.connections.values()))
                    elif cmd == 'server help':
                        print('Available commands:')
                        print('  - server exit [--force]\n  - server connections\n  - server help')
                    else:
                        print('Invalid command. Type \'server help\' to see available commands.')

    def process_request(self, sock, address):
        ''' Process client request '''
        while True:
            msg_bytes = sock.recv(1024)
        
            if msg_bytes.decode() == '':
                break
                
            msg = msg_bytes.decode()
            
            sock.send(msg.encode().upper())
    
    def exit(self):
        print('Shutting down server...')
        self.sock.close()
        print('Server is now offline.')
    
    def hasConnections(self):
        return bool(self.connections)

if(__name__ == '__main__'):
    server = Server()
    server.run()