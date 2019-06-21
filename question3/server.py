import socket
import os

class TCPServer:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = int(port)
        self.origin = (self.host, self.port)
        print('Starting server at address {} and port {}'.format(self.host,self.port))
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.tcp.bind(self.origin)
        self.tcp.listen(1)
        self.listen()
        

    def listen(self):
        conn, client = self.tcp.accept()
        print 'Connected ', client
        while True:
            msg = conn.recv(1024)
            if not msg: break
            print client, msg
        print 'Finalizando connexao do client', client
        conn.close()


if __name__ == "__main__":
    server = TCPServer(port=os.environ.get('PORT'))