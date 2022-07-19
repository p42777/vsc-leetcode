from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        hashSet = set()
        def depthFirstSearch(node):
            if not node: return False
            diff = k - node.val
            if diff in hashSet: return True
            else:
                hashSet.add(node.val)
            return depthFirstSearch(node.left) or depthFirstSearch(node.right)

        return depthFirstSearch(root)


