from datetime import datetime

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.timestamp = datetime.now()
        self.prev = None
        self.next = None


    def __str__(self):
        return "(Key: %s => Value: %s)" % (self.key, self.value)
        
    

    

        