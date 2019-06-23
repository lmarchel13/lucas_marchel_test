import socket
import os
from lru_cache import LRUCache
import pickle

class TCPServer:
    def __init__(
            self, 
            host='127.0.0.1', 
            port=4000, 
            maxSize=3, 
            expirationTimeInSeconds=300):
        
        self.host = host
        self.port = int(port)
        self.maxSize = int(maxSize)
        self.expirationTimeInSeconds = int(expirationTimeInSeconds)
        self.database = LRUCache(
                maxSize=self.maxSize,
                expirationTimeInSeconds=self.expirationTimeInSeconds
            )

        print("Starting database with {} memory capacity and expiration time of {} seconds".format(self.maxSize, self.expirationTimeInSeconds))

        self.origin = (self.host, self.port)
        print('Starting server at address {} and port {}'.format(self.host,self.port))
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.tcp.bind(self.origin)
        self.tcp.listen(10)       
        
        self.listen()

    def listen(self):       
        while True:
            try:
                self.conn, self.client = self.tcp.accept()                    
                print ('IP address {} connected!'.format(self.client[0]))
                while True:
                    msg = self.conn.recv(1024)        
                    if not msg: 
                        break
                    self.save(msg)                                        
                print('Connected closed for {}'.format(self.client[0]))        
            except:
                print('Socket error')

    def closeConnection(self):
        self.conn.close()

    def save(self, data):
        try:
            data = pickle.loads(data)
            key = data['key']
            value = data['value']
            self.database.set(key, value)            
            print('****************************')
            self.show()
            print('****************************')
        except Err:
            print('Could not save data into cache')

    def show(self):
        self.database.show()

 
if __name__ == "__main__":
    PORT = os.environ.get('PORT') or 4000
    MAX_SIZE = os.environ.get('MAX_SIZE') or 1
    EXPIRATION_TIME = os.environ.get('EXPIRATION_TIME') or 300
    server = TCPServer(port=PORT, maxSize=MAX_SIZE, expirationTimeInSeconds=EXPIRATION_TIME)    
    