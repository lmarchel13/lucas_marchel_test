import socket
import os

class TCPClient:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = int(port)
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destination = (self.host, self.port)
        self.tcp.connect(destination)
        print 'Press CTRL+X\n to exit...'

        # msg = raw_input()
        # while msg <> '\x18':
        #     tcp.send (msg)
        #     msg = raw_input()
        # tcp.close()


if __name__ == "__main__":
    client = TCPClient(port=os.environ.get('PORT'))