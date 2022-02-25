# stack using the list in python 

stack=[1,2,3,4,5,6]

stack.append(10)    #-----This function push the element in the stack

print(stack.pop())  #-----pop the element from the stack and delete from the stack

print(stack[-1])    #-----It give the last element which is inserted in the stack without deleting it   

###########################################################
# implementing the stack using the dequeue

from collections import deque
from re import S 

stack=deque()       #-----Dequeue is the double ended queue in which we can perform insert and deletion operation from both side

# print(dir(stack))   #-----Give the all information about function which is associated with dequeue 

stack.append(20)    #-----Push the element in the list

stack.appendleft(20)#-----Push the element from the left side

stack.pop()         #-----Pop the element with deleting from the stack

stack.popleft()     #-----Pop the element from the left site 

20 in stack         #-----search for 20 in the stack

stack.extend("abc") #-----Push the mutiple element in the stack

stack.extendleft("abc")#-----Push the element from the left side with reveresed order

stack.rotate()      #-----rotate the stack

stack.clear()       #-----Delete the all element from the stack

print(stack)        #-----Print the element of the stack