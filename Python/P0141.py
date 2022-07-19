class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Cycle Finding by Floyd's Algorithm

class Solution:
    def hasCycle(self, head: TreeNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # shift by 1
            fast = fast.next.next  # shift by 2
            if slow == fast:
                return True

        return False
