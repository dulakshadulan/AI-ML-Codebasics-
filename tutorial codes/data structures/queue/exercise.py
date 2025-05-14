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
    


import time
import threading

def place_order(orders):
    for food in orders:
        time.sleep(0.5)
        Q.enqueue(food)
        print(food, "ordered")

def serve_order():

    time.sleep(1)
    while True:
        if not Q.is_empty():
            time.sleep(2)
            food = Q.dequeue()
            print(food, "served")
        else:
            if not t1.is_alive():
                break
        time.sleep(0.5)

if __name__ == '__main__':
    Q = Queue()

    orders = ['pizza','samosa','pasta','biryani','burger']

    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()

    t1.join()
    t2.join()