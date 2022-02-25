"""A Set is an unordered collection data type that is iterable, 
mutable and has no duplicate elements. Python’s set class 
represents the mathematical notion of a set. The major advantage 
of using a set, as opposed to a list, is that it has a highly 
optimized method for checking whether a specific 
element is contained in the set. 
This is based on a data structure known as a hash table. 
Since sets are unordered, we cannot access items 
using indexes like we do in lists.
"""
#--set is linear data structure 
st=set()            #---Initializing the set
st2=set()

st.add(20)          #---Add the 20 in the set

st.discard(20)      #---Discard the 20 from the set

st.remove(20)       #---remove the 20 from the set

st.clear()          #---Clear all element of the set

st.copy()           #---Give the copy of set

st.difference(st2)  #---give the element which is present in the st but not present in the st2

st.intersection(st2)#---Give the commen element between the st and st2

st.union()          #---Give the set which contain the all value of st and st2

st.update(st2)      #---update the value in st of st2

