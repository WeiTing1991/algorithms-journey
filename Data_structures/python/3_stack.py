# stack
# First in / Last Out (FILO)

"""

Implementation:
list
collection.deque
queue.LifoQueue

"""
# Using a list as a stack
#
s = [] 
s.append(0)
s.append(2)
s.append(4)

print(s)

s.pop()
print(s)

print("-----------------------------------------")

# using deque stack
from collections import deque
stack = deque()
print (dir(stack)) ## iterator of deque
