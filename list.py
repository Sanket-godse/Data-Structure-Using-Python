# List is linear data structure where we can store the homogeneous or non homogeneous element
ls=[]           #-----Intializing the empty list

len(ls)         #---Give the length of the list

ls.append(10)   #----Append the 10 into the list

ls.extend([1,2,3])#----Add the multiple element in the list

type(ls)        #---Print the type of the ls which is list

ls.sort()       #----Sort the list in ascending order

ls.sort(reverse=True)#----Sort the list in descending order

ls.sort(key=len)#----Sort the element on the basis of the length of the each element

ls[-1]          #----Give the last Element of the list

ls[2:5]         #----Give the element from the 2 to 5 index

ls.index(20)    #----Give the index of the element 20 from list

ls.clear()      #----Clear the all element of the list

ls.insert(2,20) #----insert the 20 at the index 2

ls.count()      #----Give the count of total element present in the list

max(ls)         #----Give the maximum element from the list

min(ls)         #----Give the minimum element from the list

ls.pop()        #----Delete the last element with returning it

ls.remove(20)   #----remove the 20 from the list

ls.reverse()    #----reverse the list

ls[::-1]        #----reverse the list using the slicing

ls.copy()       #----Give the copy of the list

 

