class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if not root:
        root=Node(data)
    else:
        if data<root.data:
            if root.left is None:
                root.left=Node(data)
            else:
                insert(root.left,data)
        else:
            if data>root.data:
                if root.right is None:
                    root.right=Node(data)
                else:
                    insert(root.right,data)
def inorder(root):
    if root:
        inorder(root.left)    
        print(root.data,end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

root=Node(10)
ls=[6,2,0,3,12,231,52,14]
for i in ls:
    insert(root,i)
inorder(root)
print("")
preorder(root)
print("")
postorder(root)
                