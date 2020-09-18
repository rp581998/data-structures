class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

        
def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if root.data == value:
            return root
        elif root.data < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root

def search(root, data):
    if root is None or root.data == data:
        return root
    if root.data  < data:
        return search(root.right, data)
    else:
        return search(root.left, data)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
    

r = TreeNode(4)  
r = insert(r, 5)  
r = insert(r, 2)  
r = insert(r, 1)  
r = insert(r, 3)  
print(r.search(4))


inorder(r)


