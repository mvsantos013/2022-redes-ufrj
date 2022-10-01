import sys
import socket
import select
import multiprocessing

PORT = 12000

class Server():
    def run(self):
        ''' Starts server. '''
        print('Starting server...')
        print('Available commands:')
        print('  - server exit [--force]\n  - server help')

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.sock.bind(('', PORT))
        
        self.inputs = [self.sock, sys.stdin]

        print('Server is now online.')
        print(f'Listening at port {PORT}')

        while True:
            r, w, e = select.select(self.inputs, [], [])
            for ready in r:
                if ready == self.sock:
                    client = multiprocessing.Process(target=self.process_request)
                    client.start()

                elif ready == sys.stdin: 
                    cmd = input()
                    if cmd == 'server exit':
                        self.exit()
                    elif cmd == 'server help':
                        print('Available commands:')
                        print('  - server exit\n  - server help')
                    else:
                        print('Invalid command. Type \'server help\' to see available commands.')

    def process_request(self):
        ''' Process client request '''
        while True:
            msg_bytes, client_address = self.sock.recvfrom(1024)
        
            if msg_bytes.decode() == '':
                break
                
            msg = msg_bytes.decode()
            
            self.sock.sendto(msg.encode().upper(), client_address)
    
    def exit(self):
        print('Shutting down server...')
        print('Server is now offline.')
        sys.exit()
    

if(__name__ == '__main__'):
    server = Server()
    server.run()