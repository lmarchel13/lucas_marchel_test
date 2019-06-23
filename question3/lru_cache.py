# # At Ormuco, we want to optimize every bits of software we write. 
# # Your goal is to write a new library that can be integrated to the Ormuco stack. 
# # Dealing with network issues everyday, latency is our biggest problem. 
# # Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) 
# # cache with time expiration. This library will be used extensively by many of our 
# # services so it needs to meet the following criteria:

from datetime import datetime
from time import sleep
from collections import OrderedDict
from node import Node

class LRUCache(object):
    def __init__(self, maxSize = 1024, expirationTimeInSeconds = 60):        
        if maxSize <= 0:
            raise ValueError("maxSize must be bigger than 0")
        
        self.hash = OrderedDict()
        self.head = None
        self.tail = None
        self.maxSize = maxSize
        self.expirationTime = expirationTimeInSeconds
        self.length = 0

    def show(self):
        for key, value in self.hash.iteritems() :
            print(self.hash[key])                

    def size(self):
        return self.length

    def get(self, key):
        if key not in self.hash:
            return None
        
        node = self.hash[key]
        self.remove(node)
        if self.isExpired(node):            
            self.hash.pop(node.key)
            return None
        
        self.insertAfter(node)
        return node.value
        

    def set(self, key, value):  
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.remove(node)
            self.insertAfter(node)
        else:
            newNode = Node(key, value)
            if self.length == self.maxSize:
                del self.hash[self.tail.key]
                self.remove(self.tail)
            self.insertAfter(newNode)
            self.hash[key] = newNode


    def isExpired(self, node):
        now = datetime.now()
        difference = now - node.timestamp        
        if difference.seconds > self.expirationTime:
            return True
        return False

    def insertAfter(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.length += 1


    def remove(self, node):
        if not self.head:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if not node.next and not node.prev:
            self.head = None
            self.tail = None

        if self.tail == node:
            self.tail = node.next
            self.tail.prev = None

        self.length -= 1
        return node