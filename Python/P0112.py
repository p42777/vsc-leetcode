class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder Depth First Search
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def depthFirstSearch(node, currentSum):
            if not node:
                return False

            currentSum += node.val
            if not node.left and not node.right: # no leftChild & rightChild (leafNode)
                return currentSum == targetSum
            
            # return True when either the path of rightChild or leftChild == targetSum
            result = (depthFirstSearch(node.left, currentSum)) or (depthFirstSearch(node.right, currentSum)) 
            return result

        return depthFirstSearch(root, 0)

