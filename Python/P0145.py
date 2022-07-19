from ast import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def depthFirstSearch(root):
            if not root:
                return
            depthFirstSearch(root.left)
            depthFirstSearch(root.right)
            result.append(root.val)

        depthFirstSearch(root)

        return result
