from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        if root.val > val: # right subtree
            root.left = self.insertIntoBST(root.left, val)
            return root
        if root.val < val: # left subtree
            root.right = self.insertIntoBST(root.right, val)
            return root
