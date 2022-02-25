from queue import Queue

q=Queue(maxsize=3)  #---Initializing the queue with max index 3

q.qsize()           #---Give the size maxsize of queue

q.put(1)            #---Adding the element into the queue

q.get()             #---removing the element from the queue with return it

q.full()            #---Check whether queue is full or not return the boolean

q.empty()            #---Check whether queue is empty or not return the boolean


