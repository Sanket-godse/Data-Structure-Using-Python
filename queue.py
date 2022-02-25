"""Like stack, queue is a linear data structure that stores 
items in First In First Out (FIFO) manner. With a queue the 
least recently added item is removed first. A good example of 
queue is any queue of consumers for a resource where the consumer 
that came first is served first.
"""
from queue import Queue

q=Queue(maxsize=3)  #---Initializing the queue with max index 3

q.qsize()           #---Give the size maxsize of queue

q.put(1)            #---Adding the element into the queue

q.get()             #---removing the element from the queue with return it

q.full()            #---Check whether queue is full or not return the boolean

q.empty()            #---Check whether queue is empty or not return the boolean


