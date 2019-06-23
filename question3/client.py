import socket
import os
from threading import Thread
import pickle

class TCPClient(Thread):
    def __init__(self, host='127.0.0.1', port=5000):
        super(TCPClient, self).__init__()
        self.host = host
        self.port = int(port)        

    def run(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destination = (self.host, self.port)
        self.tcp.connect(destination)
        print('Client connected to {}:{}'.format(self.host, self.port))
        raw_input()

    def closeConnection(self):
        self.tcp.close()

    def sendData(self, data):   
        self.tcp.send(pickle.dumps(data))