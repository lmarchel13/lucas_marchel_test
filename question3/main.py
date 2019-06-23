from server import TCPServer
from client import TCPClient

import os
from time import sleep



if __name__ == "__main__":
    client = TCPClient('localhost', os.environ.get('PORT'))
    client.start()
    
    # time to create client
    sleep(1)
    
    for i in range(10):
        data = {'key': 'key'+str(i),'value': 'value'+str(i)}    
        client.sendData(data)
        sleep(5)
    
