#list
#collection.deque
#queue.LifoQueue
# first in first out


queue1 = []
queue1.insert(0, 100)
queue1.insert(0, 200)
queue1.insert(0, 300)

print(queue1)

queue1.pop()
print(queue1)

print("\n")

from collections import deque
queue2 = deque()
queue2.appendleft(5)
queue2.appendleft(10)
queue2.appendleft(25)

print(queue2)
queue2.pop()

print(queue2)


import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enQueue(self, val):
        self.buffer.appendleft(val)

    def deQueue(self):
        if len(self.buffer) == 0 :
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

def place_orders():
    for order in orders:
        food_order_queue.enQueue(order)
        print("Placing ", order)
        time.sleep(0.5)

def serve_oders():
    time.sleep(1)
    condition = True
    while condition:
        order = food_order_queue.deQueue()
        print("now serving ", order)
        time.sleep(2)
        if food_order_queue.size() == 0:
            condition = False
        

if __name__ == '__main__':
    
    orders = ['pizza','samosa','pasta','biryani','burger']
    
    # mutiltheading 
    t1 = threading.Thread(target=place_orders(), args=(orders,))
    t2 = threading.Thread(target=serve_oders())
    
    t1.start()
    t2.start()
    