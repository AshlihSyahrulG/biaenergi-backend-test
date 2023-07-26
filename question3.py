class Node:
    def __init__(self):
        self.right = None
        self.left = None
 
def maxDepth(node):
    if node is None:
        return 0
 
    else:
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
 
# Driver program to test above function
root = Node()
root.left = Node()
root.right = Node()
root.left.left = Node()
root.left.right = Node()
 
 
print("Height of tree is %d" % (maxDepth(root)))