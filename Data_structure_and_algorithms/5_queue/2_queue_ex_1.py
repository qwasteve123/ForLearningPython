from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self,val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[0]
    
import threading
import time as t

q = Queue()

orders = ['pizza','samosa','pasta','biryani','burger']

def place_order(orders):
    for order in orders:
        q.enqueue(order)
        t.sleep(0.5)

def serve_order():
    while q.size() > 0:
        print(q.dequeue())
        t.sleep(2)
    
t1 = threading.Thread(target=place_order,args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()

t1.join()
t2.join()
