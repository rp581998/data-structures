class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
class Tree:
    def _init__(self):
        self.root = None
        
    def insert(self, root, treeNode):
        if root is None:
            root = treeNode
        else:
            if root.data < treeNode.data:
                if root.right is None:
                    root.right = treeNode
                else:
                    insert(root.right, treeNode)
            else:
                if root.left is None:
                    root.left = treeNode
                else:
                    insert(root.left, treeNode)
        
    def inorder(root):
        if root:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

root = Tree()
root.insert(10)
root.insert(5)


