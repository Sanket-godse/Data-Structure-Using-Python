from time import sleep


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_last(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)
            
    def insert_values(self,data_list):
        self.head=None
        for i in data_list:
            # self.insert_at_last(i)
            if self.head is None:
                self.head=Node(i,None)
            else:
                itr=self.head
                while itr.next:
                    itr=itr.next
                itr.next=Node(i,None)
    def get_len(self):
        c=1
        if self.head is None:
            return 0
        else :
            itr=self.head
            while itr.next:
                itr=itr.next
                c+=1
        return c
    
    def remove(self,ind):
        if ind>self.get_len():
            print("invalid index..")
        if ind<0 and self.get_len()>ind:
            print("Not valid index")
        if ind==0:
            self.head=self.head.next
            return
        else :
            itr=self.head
            c=0
            while itr.next:
                if c==ind-1:
                    itr.next=itr.next.next
                    break
                itr=itr.next
                c+=1
    
    def print(self):
        temp=''
        if self.head is None:
            print("linked list is empty")
            
        else :
            itr=self.head
            while itr:
                temp=str(temp)+str(itr.data)+"-->"
                itr=itr.next
            print(temp)
            print("len is : ",self.get_len())

        
if __name__=="__main__":
    ll=LinkedList()
    # ll.insert_at_beg(10)
    # ll.insert_at_beg(20)
    # ll.insert_at_last(10)
    # ll.insert_at_last(20)
    # print(ll.get_len())
    ll.insert_values([10,20,3,0,2,5,6,9,8,5,11])
    ll.print()
    ll.remove(10)
    ll.print()

