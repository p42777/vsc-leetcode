from ast import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []  

        def depthFirstSearch(root):
            if not root:  
                return
            result.append(root.val)
            depthFirstSearch(root.left)
            depthFirstSearch(root.right)

        depthFirstSearch(root)

        return result
