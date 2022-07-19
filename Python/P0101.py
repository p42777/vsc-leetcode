class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetricRecursive(root.left, root.right)

    def isSymmetricRecursive(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False

        # compare leftChild of leftNode and rightChild of rightNode
        return self.isSymmetricRecursive(left.left, right.right) and self.isSymmetricRecursive(left.right, right.left)

